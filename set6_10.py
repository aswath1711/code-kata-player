# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:23:08 2019

@author: New
"""


a,b=input().split()
a=list(a)
p=0
b=list(b)
for i in range(len(a)):
    if a[i] in b:
        p=1
if p==1:
    print('yes')
else:
    print('no')