# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 19:54:30 2019

@author: New
"""

l=int(input())
li=list(map(str,input().split()[:l]))
li.sort()
li.sort(key=len)
for i in li:
    print(i,end=" ")