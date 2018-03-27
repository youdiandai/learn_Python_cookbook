#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/27'
"""
"""
从任意长度的可迭代对象中分解元素
"""


a=[1,2,3,4,5,6,7,8]
b,c,*d = a
print(b)
#使用*表达式可以实现，*后面的变量名代表了多出来的元素


def sum(items):
    head,*tail = items
    return head+sum(*tail) if tail else head
#实现递归,如果有尾就返回头加上尾的和，没有就返回头
#Python不擅长递归，能不用就不用