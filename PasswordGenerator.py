# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:27:53 2021

@author: Dean321

Password generator includes both easy and difficult level
    Eazy Level - Order not randomised:
        e.g. 4 letter, 2 symbol, 2 number = JduE&!91
    Hard Level - Order of characters randomised:
        e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:

l = []

total = nr_letters+nr_symbols+nr_numbers
for i in range(0,nr_letters):
    r = random.randint(0,len(letters)-1)
    l.append(letters[r])
for i in range(0,nr_symbols):
    r = random.randint(0,len(symbols)-1)
    l.append(symbols[r])
for i in range(0,nr_numbers):
    r = random.randint(0,len(numbers)-1)
    l.append(numbers[r]) 
s = ""
for i in l:
    s+=i
print(s)



#Hard Level - Order of characters randomised:

total = nr_letters+nr_symbols+nr_numbers
s = ""
rl = []
for i in range(0,total+1):
    r = random.randint(0,len(l)-1)
    if r not in rl:
        rl.append(r)
        s+=l[r]
    else:
        total+=1

s=""
random.shuffle(l)
for i in l:
    s+=i
print(s)


















