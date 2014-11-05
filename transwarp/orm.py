# -*- encoding: utf-8 -*-
'''
Created on 2014-11-5

@author: huangtx@itg.net
'''
from transwarp import db


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        
        db.select('')
        attrs['__table__'] = cls.__table__
        return type.__new__(cls, name, bases, attrs)
    
    
class Model(dict):
    __metaclass__ = ModelMetaclass
    def __init__(self, **kw):
        super(Model, self).__init__(self, **kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except:
            raise KeyError('不存在此字段')
    def __setattr__(self, key, value):
        self[key] = value
        
        

        
