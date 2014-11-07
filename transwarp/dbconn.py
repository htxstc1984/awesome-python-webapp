# -*- encoding: utf-8 -*-
import ConfigParser

import MySQLdb
import pymssql

class Dbconn(dict):
    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.readfp(open('../conf/db.ini'))
        self.initParas = {k:v for k, v in config.items('global')}
        print self.initParas
        for v in ('drivername', 'host', 'port', 'user', 'passwd', 'db'):
            if not v in self.initParas.keys():
                raise NameError('配置信息不完整')
#         print config.get("global", "host")
        
    def init(self, *args, **kw):
        if(self.initParas['drivername'] == 'mysql'):
            p = self.initParas
            return MySQLdb.connect(host=p['host'], port=int(p['port']), user=p['user'], passwd=p['passwd'], charset=p['charset'], db=p['db'])
        elif(self.initParas['drivername'] == 'mssql'):
            p = self.initParas
#             return pymssql.connect(host=p['host'], user=p['user'], password=p['passwd'], database=p['db'],charset='utf8')
        else:
            raise BaseException('不支持此数据库')
    
            
