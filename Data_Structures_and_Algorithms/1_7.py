#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/28'
"""
from collections import OrderedDict
import json
"""
有序的字典
"""


d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
#OrderedDict构建的字典会记录元素添加的顺序
#在稍后需要对字典做序列化或者编码为另外一种格式时有用，比如要生成一个字段有顺序的json
b= json.dumps(d)
#生成的字典的大小是普通字典的两倍多，如果要构建特别大的OrderedDict字典，要好好考虑需求


if __name__ == '__main__':
    print(d)
    print(b)
