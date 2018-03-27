#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/27'
"""
"""
保存最后N个元素
"""
from collections import deque
#deque为list添加append，pop，appendleft和popleft，可以方便的往list头和尾添加元素
#相当于实现了队列了

def search(lines,pattern,history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line :
            yield line,previous_lines
        previous_lines.append(line)

#队列的头和尾处添加和移除元素的复杂度都是O(1)
#列表头部添加删除元素的复杂度是O(N)
