# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:40:56 2019

@author: New
"""

a=input()
l=[]
s=[]
for i in range(0,len(a)):
  if(a[i]=='('):
    l.append(a[i])
  elif(a[i]==')'):
    s.append(a[i])
if(len(l)==len(s)):
  print("yes")
else:
  print("no")
© 2019 GitHub, Inc.
