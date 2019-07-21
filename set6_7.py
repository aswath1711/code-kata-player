# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:11:31 2019

@author: New
"""

a,b=input().split()
p=0
for i in range(len(a)):
    if a[i]==b:
        p+=1
print(p)