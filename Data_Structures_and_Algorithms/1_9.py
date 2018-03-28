#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/28'
"""
"""
两个字典寻找相同点
"""
a = {
    'x':1,
    'y':2,
    'z':3
}
b = {
    'w':10,
    'x':11,
    'y':2
}
#find keys in common
a.keys() & b.keys()

#find keys in a that are not in b
a.keys() - b.keys()

c = {key:a[key] for key in a.keys() - {'z','w'}}
#字典推导式，去掉a中的z，和w
#字典的键可以支持常见的集合操作