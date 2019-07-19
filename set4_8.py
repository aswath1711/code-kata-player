# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:09:40 2019

@author: New
"""

n=int(input())
l=[]
for i in rannge(n):
    if n%i==0:
        l.append(i)
print(*l)