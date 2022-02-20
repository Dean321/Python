# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:56:25 2021

@author: Dean321

A simple program to find the highest bid 
"""

print('''
                        _   _             
                 | | (_)              
  __ _ _   _  ___| |_ _  ___  _ __  
 / _` | | | |/ __| __| |/ _ \| '_ \ 
| (_| | |_| | (__| |_| | (_) | | | |
 \__,_|\__,_|\___|\__|_|\___/|_| |_|
      
 __      ____ _ _ __ 
\ \ /\ / / _` | '__|
 \ V  V / (_| | |   
  \_/\_/ \__,_|_|
  
    ''')
choice = "y"
d = {}
while choice == "y" or choice == "Y":
    name = input("Enter your name here: ")
    amt = int(input("Enter amount here: ₹"))
    d[name] = amt
    choice = input("Is there another bid type y - yes or n - no: ")
ans = 0
winner = ""
for key in d:
    if d[key]>=ans:
        ans = d[key]
        winner = key
print(f"The winning bid is of {winner} of ₹{ans}")