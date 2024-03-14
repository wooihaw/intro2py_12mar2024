# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:27:21 2024

@author: wooihaw
"""

s1 = set(range(1, 101))
s2 = set(range(5, 101, 5))  # the numbers divisible by 5
s3 = set(range(7, 101, 7))  # the numbers divisible by 7

print(list(s1 - (s2 | s3)))
