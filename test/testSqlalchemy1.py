#-*- encoding: utf-8 -*-
'''
Created on 2014-11-5

@author: huangtx@itg.net
'''
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative.api import declarative_base
from sqlalchemy.orm import create_session, relation
from sqlalchemy.orm.session import sessionmaker, Session
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String, Integer, Text


Base = declarative_base()
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' % ('root', 'root', '172.16.109.105:3306', 'itgfz2014'))

class Member(Base):
    __tablename__ = 'itgfz_member'
    
    userid = Column(String(20),primary_key = True)
    username = Column(String(20))
    passport = Column(String(20))
    email = Column(String(20))
    recmsg = relation('Message',backref='itgfz_message')
    sendmsg = relation('Message',backref='itgfz_message')
    
class Message(Base):
    __tablename__ = 'itgfz_message'
    
    itemid = Column(Integer,primary_key = True)
    title = Column(String(20))
    content = Column(Text)
    touser = Column(Integer,ForeignKey('itgfz_member.username'))
    fromuser = Column(Integer,ForeignKey('itgfz_member.username'))
    
class Info_24(Base):
    __tablename__ = 'itgfz_info_24'
    itemid = Column(Integer,primary_key = True)
    catid = Column(Integer)
    title = Column(String(50))
#     data = relation('Info_data_24',backref='itgfz_info_data_24')
    
class Info_data_24(Base):
    __tablename__ = 'itgfz_info_data_24'
    itemid = Column(Integer,primary_key = True)
    content = Column(Text)
#     pid = Column('itemid',Integer,ForeignKey('itgfz_info_24.itemid'))
    

if __name__ == '__main__':
    session = create_session(bind=engine)
#     session = Session(bind=engine)
    query = session.query(Member).filter(Member.userid=='1')
    ms = query.all()
    for m in ms:
        for s in m.recmsg:
            print s.title
    print [m.recmsg for m in ms]

    pass











