# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:57:34 2019

@author: New
"""

n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
print(l[k])
