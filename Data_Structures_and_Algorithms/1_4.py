#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/27'
"""
"""
找到最大或最小的N个元素
"""
from heapq import nlargest,nsmallest
#headq有一大部分堆操作

nums = [1,8,2,23,7,-4,18,23,42,37,2]
print(nlargest(3,nums))
print(nsmallest(3,nums))
