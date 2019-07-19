# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 23:42:23 2019

@author: New
"""

import math
n1=int(input())
n=math.radians(n1)
if (n>0 and n<1):
    print(round(math.sin(n),2))
else:
    print(round(math.sin(n)))