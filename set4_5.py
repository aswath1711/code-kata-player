# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 21:13:16 2019

@author: New
"""

import string
a=input()
a.split()
a=a.replace(" ","")
b=[i for i in a if a.count(i)==1]
c=' '.join(b)
print(c.lower())
