#-*- encoding: utf-8 -*-
'''
Created on 2014-11-7

@author: huangtx@itg.net
'''
from jinja2 import Environment,PackageLoader,runtime


if __name__ == '__main__':
    
    env = Environment(loader=PackageLoader('www', 'templates'),undefined=runtime.Undefined,line_statement_prefix='##',trim_blocks=False)
    temp = env.get_template('testHtml.html')
    paras = dict()
    paras['name'] = 'htx'
    paras['wel'] = u'欢迎您!11111'
    print temp.render(**paras)
    pass