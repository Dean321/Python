# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:33:08 2022

@author: Dean321
"""
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
d = {j.letter:j.code for i,j in df.iterrows()}
# print(d)
name = input("Enter your name here: ")
name_list = [d[i.upper()] for i in name]
print(name_list)
