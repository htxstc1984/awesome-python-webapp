# -*- encoding: utf-8 -*-
'''
Created on 2014-11-7

@author: huangtx@itg.net
'''

import pymongo
from pymongo.database import Database
from pymongo.mongo_client import MongoClient
from pymongo.collection import Collection

if __name__ == '__main__':
    con = pymongo.Connection('172.16.10.170', 27017)
    db = Database(con, 'test')
    coll = Collection(db, 'foo')
#     coll.insert({'a':1, 'b':2, 'c':3})
    coll.update({'a':1}, {'$set':{'b':4}},multi=True)
    print [x for x in coll.find()]
#     MongoClient()
#     print user.find({'id':1}).count()
    pass
