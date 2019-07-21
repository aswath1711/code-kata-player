# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:14:30 2019

@author: New
"""


a=list(map(str,input().split()))
p=0
b=input()
for i in range(len(a)):
    if a[i]==b:
        p+=1
print(p)