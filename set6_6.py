# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:07:13 2019

@author: New
"""

a,b=input().split()
p=-1
for i in range(len(a)):
    if a[i]==b:
        p=i
        break
print(p+1)
        