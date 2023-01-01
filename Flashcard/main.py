# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 12:35:54 2023

@author: Dean321
"""
BACKGROUND_COLOR = "#F5EFE6"
FLASHCARD_COLOR = "#AEBDCA"
TITLE_COLOR = "#E8DFCA"
WORD_COLOR = "#7895B2"
FONT_NAME = 'Roboto Slab'

import random
import pandas as pd
from tkinter import *
import pyglet
import time



pyglet.font.add_file('RobotoSlab-VariableFont_wght.ttf')


df = pd.read_csv("data.csv")
# print(df)
data = df.to_dict()
# print(data)
lod = len(data["Word"])
rw = random.randint(0,lod-1)
wrd = data["Word"][rw]
unknown_words = {"Word":[],"Meaning":[]}
def chk(m):
    # print(m, len(m))
    if len(m)>50 and len(m)<100:
        d=2
    elif len(m)>=100:
        d=3
    else:
        return m
    s = m.split()
    h = round(len(s)/d)
    cnt = 0
    ns = ''''''
    for i in s:
        if cnt<=h:
            ns=ns+i+" "
            cnt+=1
        else:
            cnt=0
            ns+="\n"
            
    # print("new m => ",ns,"\n\n")
    return ns

global m
m = ""
m = chk(data["Meaning"][rw])


def getWord():
    l = len(data["Word"])
    r = random.randint(0,l-1)
    w = data["Word"].get(r)
    while w==None:
        r = random.randint(0,l-1)
        w = data["Word"].get(r)
    
    global m, flip_timer 
    window.after_cancel(flip_timer)
    m = ""
    m = chk(data["Meaning"][r])
    # print(63,m)
    canvas.configure(bg=FLASHCARD_COLOR)
    canvas.itemconfig(title, text="Word", fill=TITLE_COLOR)
    canvas.itemconfig(word, text=w, fill=WORD_COLOR, font=(FONT_NAME, 45, "bold"))
    flip_timer = window.after(3000, func=flipcard)
    return r
def flipcard():
    canvas.itemconfig(title, text="Meaning", fill=FLASHCARD_COLOR)
    canvas.itemconfig(word, text=m, fill=TITLE_COLOR, font=(FONT_NAME, 18))
    canvas.configure(bg=WORD_COLOR)

def right():
    r = getWord()
    for k in data.keys():
        del data[k][r]
        
def wrong():
    r = getWord()
    uw = data["Word"][r]
    um = data["Meaning"][r]
    # unknown_words.update({uw:um})
    unknown_words["Word"].append(uw)
    unknown_words["Meaning"].append(um)
    udf = pd.DataFrame(unknown_words)
    udf.to_csv("words_to_learn.csv")
    
window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.iconbitmap("logo.ico")
flip_timer=window.after(3000, func=flipcard)

canvas = Canvas(width=600, height=300, bg=FLASHCARD_COLOR, highlightthickness=0)
title = canvas.create_text(300, 50, text="Word", fill=TITLE_COLOR, font=(FONT_NAME, 20))
word = canvas.create_text(300, 150, text=wrd, fill=WORD_COLOR, font=(FONT_NAME, 45, "bold"))
canvas.grid(column=0, row=0, columnspan=3)

rightImg = PhotoImage(file="right.png")
rightBtn = Button(image=rightImg, highlightthickness=0, width=100, height=100, bg=BACKGROUND_COLOR,borderwidth=0,command=right)
rightBtn.grid(column=0,row=1,pady=10)

wrongImg = PhotoImage(file="wrong.png")
wrongBtn = Button(image=wrongImg, highlightthickness=0, width=100, height=100, bg=BACKGROUND_COLOR,borderwidth=0,command=wrong)
wrongBtn.grid(column=2, row=1)



window.mainloop()