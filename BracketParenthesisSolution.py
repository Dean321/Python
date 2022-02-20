# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:56:07 2021

@author: Dean321
"""

s =  "(((?" #"(?][" #"[(?][??["
s_l = [a for a in s if a !="?"]
l=['{', '}', '[', ']', '(', ')']
q_c = s.count("?")
o = ["[","{","("]
c = ["]","}",")"]
cnt = 0
l_i=0
check=""
for i in s_l:
    if i in o:
        index = o.index(i)
        change = c[index]
    else:
        index = c.index(i)
        change = o[index]
    if change in s_l:
        temp = s_l.index(i)
        s_l[temp]+=change
        s_l.remove(change)
        cnt+=1
    else:
        if q_c!=0:
            temp = s_l.index(i)
            s_l[temp]+=change
            cnt+=1
            q_c-=1
        else:
            cnt=0
if cnt!=0:
    cnt/=2
print(int(cnt))
