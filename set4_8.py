# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:09:40 2019

@author: New
"""

n=int(input())
l=[]
for i in range(1,n):
    if n%i==0:
        l.append(i)
for j in l:
    if(j%2==0):
        print(j,end=" ")
