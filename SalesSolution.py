# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 14:20:37 2021

@author: Dean321
"""
import math
n = 7
ar = [1,2,1,2,1,3,2,2,3,2,3,4,4]
cnt = 0
s = list(set(ar))
for i in s:
    tot = ar.count(i)
    cnt += int(tot/2)
    
print(cnt)