#-*- encoding: utf-8 -*-
'''
Created on 2014-11-5

@author: huangtx@itg.net
'''
from sqlalchemy.sql.schema import MetaData, Table


metadata = MetaData('mysql://%s:%s@%s/%s?charset=utf8' % ('root', 'root', '172.16.109.105:3306', 'itgfz2014'))

if __name__ == '__main__':
    
    mem_tab = Table('itgfz_member',metadata,autoload=True)
    
    stat = mem_tab.select()
    print stat
    r = stat.execute()
    print [v for v in r.fetchall()]
    
    pass




