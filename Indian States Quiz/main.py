# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:02:03 2022

@author: Dean321
"""

import turtle
import pandas as pd

df = pd.read_csv("indian_states.csv")
all_states = df["state"].to_list()
guessed_states=[]
screen = turtle.Screen()
screen.title("Indian States & Union Territories Quiz")
img = "indianMap.gif"
screen.addshape(img)
turtle.shape(img)

while len(guessed_states)<36:
    
    answer_state = screen.textinput(title=str(len(guessed_states)) + "/36 states correct", prompt="What's another state?")
    answer_state = answer_state.title()
    # print(answer_state)
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = df[df.state==answer_state]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(answer_state)
if len(guessed_states) != 50:
    missed_states = []    
    for i in all_states:
        if i not in guessed_states:
            missed_states.append(i)
    print("States missed: \n",missed_states)      
    new_data = pd.DataFrame(missed_states)
    new_data.to_csv("missed_sates.csv")

screen.exitonclick()