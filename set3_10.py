# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:17:30 2019

@author: New
"""

a,b,l=map(str,input().split())
a=list(a)
b=list(b)
count=0
for i in range(0,len(a)):
        if(a[i]!=b[i]):
            count=count+1
if(count==int(l)):
    print("yes")
else:
    print("no")
