# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:43:34 2019

@author: New
"""
a,b=map(int,input().split())
p=0
c=0
f=0
while(p<a):
    p=b**c
    if p==a:
        f=1
    c=c+1
if f==0:
    print('no')
else:
    print('yes')