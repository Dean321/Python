# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:15:45 2021

@author: Dean321
"""
a = [1,2,3,4,5,6]
a_l = len(a)
ans=[]
f_ans = []
sum=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i:j] not in ans:
            ans.append(a[i:j])
            sum=0
            for n in a[i:j]:
                sum+=n
            f_ans.append(sum)
f_ans.sort(reverse=True)
print(f_ans)
