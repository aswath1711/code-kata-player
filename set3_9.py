# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:13:17 2019

@author: New
"""

import math
l,r=map(int,input().split())
count=0
for i in range(l,r+1):
    p=math.sqrt(i)
    if math.sqrt(i)==int(p):
        count+=1
print(count)