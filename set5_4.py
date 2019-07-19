# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:07:23 2019

@author: New
"""
from collections import deque
n,k=map(str,input().split())
k=int(k)
items = deque(n)
items.rotate(k)

print(''.join(items))  # 'OHELL'
