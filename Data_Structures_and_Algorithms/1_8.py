#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'changxin'
__mtime__ = '2018/3/28'
"""
"""
对字典做各种计算，比如求最大最小值等
"""
prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75
}

min_price = min(zip(prices.values(),prices.keys()))
print(min_price)
max_price = max(zip(prices.values(),prices.keys()))
print(max_price)

#zip()可以将几个序列里面的值根据位置创建元组，比如序列1和序列2的第一个元素就会构成第一个元组，以此类推
#zip创建的是一个元组，访问一次返回一个元组
#max和min进行排序时还可以用lambad函数产生一个key，将对key进行排序