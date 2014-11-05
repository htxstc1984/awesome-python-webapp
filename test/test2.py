# -*- encoding: utf-8 -*-
import threading

from transwarp import db
from encodings import latin_1

def doSelect():
    result = db.select('select * from itgfz_member where company like \'%%%s%%\'' % u'国贸')
#     result = db.select('select top 20 psnname from bd_psndoc')
    
    for r in result:
        print r
#         print r['psnname'].encode('iso8859-1').decode('gbk').encode('utf-8')
#     ctx = db._db_ctx
#     ctx.aa = threading.current_thread().name
#     print threading.current_thread().name + ":" + str(ctx)
#     cur = ctx.cursor()
#     members = cur.execute("select * from itgfz_member")
#     
#     for member in cur.fetchmany(members):
#         print member

# class MyThread(threading.Thread):
#     def run(self):
#         for i in range(3):
#             doSelct(i)
# def test():
#     for i in range(5):
#         t = MyThread()
#         t.start()
# 
# test()

# for i in range(3):
#     t = threading.Thread(target=doSelct)
#     t.start()
#     t.join()

if __name__ == '__main__':
    
    doSelect()
        
    print threading.current_thread().name + ':' + db._db_ctx.aa
