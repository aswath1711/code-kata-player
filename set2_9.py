# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:37:15 2019

@author: New
"""

a=int(input())
l=[]
for i in range (2,a+1):
    if(a%i)==0:
        l.append(i)
        a=a//i
s=sorted(l)
print(*s)