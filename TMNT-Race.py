# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:23:41 2021

@author: Dean321
"""
from turtle import *
import random


colors = [(1.0, 0.0, 0.0),(0.5450980392156862, 0.0, 0.5450980392156862),(1.0, 0.27058823529411763, 0.0),(0.0, 0.0, 0.5450980392156862)]#"#FF0000", "#8B008B", "#FF4500", "#00008B"]
names = ["Donatello", "Raphael", "Michelangelo", "Leonardo"]
turtles = []
position = [-40, -10, 20, 50, 80, 110]
flag = False
winner = ""


screen = Screen()
screen.setup(width=500, height=400)


user_text = screen.textinput("Make your bet", "Which Ninja-turtle will win the race? Enter their name:  ")
print(user_text)

for i in range(0,4):
    temp = Turtle(shape="turtle")
    temp.color(colors[i])
    temp.penup()
    temp.goto(x = -230, y=position[i])
    turtles.append(temp)
    
if user_text:
    flag = True

while flag:
    for i in turtles:
        if i.xcor() >230:
            temp = i.pencolor()
            index = colors.index(temp)
            winner = names[index]
            flag = False
        dist = random.randint(0, 10)
        i.forward(dist)

if user_text == winner:
    print("You won the bet")
else:
    print("%s won. Sorry you loose"%winner)
        
    






screen.exitonclick()