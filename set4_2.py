# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:59:29 2019

@author: New
"""

n,k=map(int,input().split())
n=list(map(int,input().split()))
if k in n:
    print('Yes')
else:
    print('No')