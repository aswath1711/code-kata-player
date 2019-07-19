# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:37:30 2019

@author: New
"""

a,b=map(str,input().split())
count=0
for i in a:
    if int(i)==int(b):
        count+=1
print(count)