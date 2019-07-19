# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:07:23 2019

@author: New
"""
import collections
s=None
k,n=map(str,input().split())
de=collections.deque(list(k))
s=de.rotate(int(n))
print(s)
