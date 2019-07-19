# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 22:53:26 2019

@author: New
"""

n=int(input())
lis1=list(map(int, input().split()))
lis2=lis1
lis1.sort()
f=0
for i in range(n):
    if lis2[i]!=lis1[i]:
        f=1
if f==1:
    print('no')
else:
    print('yes')