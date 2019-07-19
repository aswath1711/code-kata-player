# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:44:48 2019

@author: New
"""
n=int(input())
f=0
for i in range(0,n):
  if(2**i==n):
    f=1
if(f==1):
   print("yes")
else:
  print("no")
