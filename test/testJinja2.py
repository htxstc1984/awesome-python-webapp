#-*- encoding: utf-8 -*-
'''
Created on 2014-11-7

@author: huangtx@itg.net
'''
from jinja2 import Environment,PackageLoader


if __name__ == '__main__':
    
    env = Environment(loader=PackageLoader('www', 'templates'))
    temp = env.get_template('testHtml.html')
    paras = dict()
    paras['name'] = 'htx'
    print temp.render(**paras)
    pass