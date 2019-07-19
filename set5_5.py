# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:32:40 2019

@author: New
"""

n2,k=map(int,input().split())
p=(n2//2)-1
for i in range(1,p+1):
  if i*p==k:
    print("yes")
    break
  else:
    p-=1
else:
  print("no")