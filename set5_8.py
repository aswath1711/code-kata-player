# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:51:48 2019

@author: New
"""

n=int(input())
l=[]
for i in range(1,n+1):
    if n%i==0 and i%2!=0:
        l.append(i)      
for i in range(len(l)-1):
    print(l[i],end=' ')
print(l[len(l)-1],end='') 