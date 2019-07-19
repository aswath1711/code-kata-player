# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:40:56 2019

@author: New
"""

str=raw_input()
li=list(str)
count1=0
count2=0
for i in li:
    if i=='(':
        count1+=1
    if i==')':
        count2+=1
if count1==count2:
    print("yes")
else:
    print("no")