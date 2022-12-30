# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 13:33:08 2022

@author: Dean321
"""
import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
d = {j.letter:j.code for i,j in df.iterrows()}


def genNATO():
    name = input("Enter your name here: ")
    try:
        name_list = [d[i.upper()] for i in name]
    except KeyError:
        print("Sorry only type letters please")
        genNATO()
    else:
        print(name_list)


genNATO()
