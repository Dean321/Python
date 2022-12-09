# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:11:48 2022

@author: Dean321
"""

morse_codes = {
    "A":".-",
    "B":"-...",
    "C":".-.-",
    "D":"-..",
    "E":".",
    "F":"..-.",
    "G":"--.",
    "H":"....",
    "I":"..",
    "J":".---",
    "K":"-.-",
    "L":".-..",
    "M":"--",
    "N":"-.",
    "O":"---",
    "P":".--.",
    "Q":"--.-",
    "R":".-.",
    "S":"...",
    "T":"-",
    "U":"..-",
    "V":"...-",
    "W":".--",
    "X":"-..-",
    "Y":"-.--",
    "Z":"--..",
    " ":" ",
    "\n":"\n"    
}

text = input("Enter text: ")
for i in text:
    I = i.upper()
    if I in morse_codes:
        print(morse_codes[I],end="")
        
        
