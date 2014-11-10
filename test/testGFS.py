#-*- encoding: utf-8 -*-
'''
Created on 2014-11-10

@author: huangtx@itg.net
'''

import StringIO
import os
import threading

import Image
from bson.objectid import ObjectId
from gridfs import *
import pymongo
from pymongo.connection import Connection
from pymongo.database import Database

class GFS:
    con = None
    fs = None
    file = None
    fl = None
    db = None
    instance = None
    locker = threading.Lock()
    
    @staticmethod
    def _conn():
        if not GFS.con:
            GFS.con = pymongo.Connection('172.16.10.170', 27017)
            GFS.db = Database(GFS.con,'test')
            GFS.fs = GridFS(GFS.db, 'images')
            
    def __init__(self):
        print 'init...'
        self._conn()
        print "server info " + " * " * 40
        print GFS.con.server_info
    
    @staticmethod    
    def getInstance():
        GFS.locker.acquire()
        try:
            if not GFS.instance:
                GFS.instance = GFS()
            return GFS.instance
        finally:
            GFS.locker.release()
            
    #写入
    def put(self, name,  format="png",mime="image"):
        gf = None
        data = None
        try:
            data = StringIO.StringIO()
#             name = "%s.%s" % (name,format)
            image = Image.open(name)
            image.save(data,format)
            #print "name is %s=======data is %s" % (name, data.getvalue())
            gf = GFS.fs.put(data.getvalue(), filename=name, format=format)
        except Exception as e:
            print "Exception ==>> %s " % e
        finally:
            GFS.con = None
            GFS._conn()
        return gf

    #获得图片
    def get(self,id):
        gf = None
        try:
            gf  = GFS.fs.get(ObjectId(id))
            im = gf.read()                  #read the data in the GridFS
            dic = {}
            dic["chunk_size"] =  gf.chunk_size
            dic["metadata"] = gf.metadata
            dic["length"] = gf.length
            dic["upload_date"] = gf.upload_date
            dic["name"] = gf.name
            dic["content_type"] = gf.content_type
#             dic["format"] = gf['format'] or 'none'
            return (im , dic)
        except Exception,e:
            print e
            return (None,None)
        finally:
            if gf:
                gf.close()
    
    
    #将gridFS中的图片文件写入硬盘
    def write_2_disk(self, data, dic):
        name = r'./get_%s.png' % 'aa'
        if name:
            output = open(name, 'wb')
            output.write(data)
            output.close()
            print "fetch image ok!"
    
    #获得文件列表
    def list(self):
        return GFS.fs.list()

if __name__ == '__main__':
    gfs = GFS.getInstance()
#     objid = gfs.put(unicode(r'C:\Users\huangtx@itg.net\Desktop\招聘微信\图片处理\2-7-b.PNG' , "utf8"))
#     print gfs.get(objid)
#     print gfs.get("5460672bf7e8f62b4ce35975",write2file)
    (data, dic) = gfs.get(ObjectId('5460672bf7e8f62b4ce35975'))
    gfs.write_2_disk(data, dic)
#     print gfs.list()
    pass