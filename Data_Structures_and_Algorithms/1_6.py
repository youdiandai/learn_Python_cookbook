#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/28'
"""
"""
可以一个键映射多个值的字典，multidict
"""
"""
可以用元组或者列表做字典的值
"""
from collections import defaultdict
#defaultdict可以创建一个multidict
#与记录分组有很强关联
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(3)

f = {}
pairs = {(1,2),(3,4),(5,6)}
for key,value in pairs:
    if key not in f:
        f[key] = []
    f[key].append(value)

g = defaultdict(list)
for key,value in pairs:
    g[key].append(value)

if __name__ == '__main__':
    print(d)
    print(e)
    print(f)
    print(g)