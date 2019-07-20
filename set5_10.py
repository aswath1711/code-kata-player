# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:50:04 2019

@author: New
"""

num = int(input())
a =0
for i in range(2,num):
    if num%i ==0:
        a = 1
        print("yes")
        break
if a==0:
    print("no")