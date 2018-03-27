#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/27'
"""
"""
优先级队列
"""
"""
一个队列根据给定的优先级来进行排列，每次pop操作返回优先级最高的那个元素
"""

import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self.index,item))
        self._index +=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

#一个优先级队列