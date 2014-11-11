#-*- encoding: utf-8 -*-
import threading

from transwarp.dbconn import Dbconn
import types


class _Engine(object):
    def __init__(self, connect):
        self.connect = connect
    def connect(self):
        return self.connect
    
engine = None

class _DbCtx(threading.local):
    def __init__(self):
        self.connection = None
        self.transcations = 0
        self.aa = threading.current_thread().name
        
    def is_init(self):
        return not self.connection is None
    
    def init(self, **kw):
        dbconn = Dbconn()
        self.connection = dbconn.init()
        self.transcations = 0
        
    def cleanup(self):
        self.connection.cursor().close()
        self.connection.close()
        self.connection = None
        
    def cursor(self):
        return self.connection.cursor()
    
_db_ctx = _DbCtx()

class _ConnectionCtx(object):
    def __init__(self):
        pass
    def __enter__(self):
        global _db_ctx
        self.should_cleanup = False
        if not _db_ctx.is_init():
            _db_ctx.init()
            self.should_cleanup = True
        return self
    
    def __exit__(self, *args):
        global _db_ctx
        if self.should_cleanup:
            _db_ctx.cleanup()

def connection():
    return _ConnectionCtx()

def with_connection():
    def decorator(func):
        def wrapper(*args, **kw):
            if not _db_ctx.is_init():
                _db_ctx.init()
            rs = func(*args, **kw)
            _db_ctx.cleanup()
            return rs
        return wrapper
    return decorator

def with_transcation():
    def decorator(func):
        def wrapper(*args, **kw):
            if not _db_ctx.is_init():
                _db_ctx.init()
            _db_ctx.transcations = _db_ctx.transcations + 1
            rs = func(*args, **kw)
            _db_ctx.transactions = _db_ctx.transactions - 1
            try:
                if _db_ctx.transactions == 0:
                    commit()
                    return rs
            except:
                rollback()
            finally:
                _db_ctx.cleanup()
            
            return None
        return wrapper
    return decorator

def commit(self):
    global _db_ctx
    try:
        _db_ctx.connection.commit()
    except:
        _db_ctx.connection.rollback()
        raise

def rollback(self):
    global _db_ctx
    _db_ctx.connection.rollback()
   
@with_connection() 
def select(sql, *args):
    global _db_ctx
    cur = _db_ctx.cursor()
    num = cur.execute(sql, *args)
    print u'查询语句：' + sql + u'，共有' + str(num) + u'条记录'
    print cur.description
#     records = [x for x in cur.fetchall()]
    records = []
    for line in cur.fetchall():
        record = dict()
        for i,v in enumerate(line):
#             record[cur.description[i][0]] = unicode(v.encode('iso8859-1').decode('gbk').encode('utf-8')) if isinstance(v, types.UnicodeType) else v
            record[cur.description[i][0]] = v
        records.append(record)
    return records
#         print line
#     return (x for x in cur.fetchall())
        
    
