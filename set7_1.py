# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 16:27:44 2019

@author: New
"""

a,b=list(map(int,input().split()))
l=list(map(int,input().split()))
c=0
for i in range(a-1):
  for j in range(1,a):
    if l[i]+l[j]==b:
      c=1
if c==0:
  print("no")
else:
  print("yes")