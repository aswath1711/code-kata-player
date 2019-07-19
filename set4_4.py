# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:07:35 2019

@author: New
"""

s=str(input())
ns=""
for i in range(0,len(s)):
    if(i%3==0):
        ns=ns+s[i]
print(ns)