# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:07:23 2019

@author: New
"""
import collections
k,n=map(str,input().split())
de=collections.dequeue(k)
print(de.rotate(int(n)))