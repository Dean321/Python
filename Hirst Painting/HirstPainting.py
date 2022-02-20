# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 10:59:19 2021

@author: Dean321
"""
import colorgram
from turtle import *
import random

rgb_colors = []
colors = colorgram.extract("point.jpg", 30)
for color in colors:
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
    
print(rgb_colors)

t = Turtle()
t.shape("turtle")
t.speed("fastest")
t.penup()
screen = Screen()
screen.colormode(255)

for i in range(1,11):
    if i%2==0:
        for _ in range(10):
            t.color(random.choice(rgb_colors))
            t.dot()
            t.forward(20)
           
        t.right(90)
        t.forward(20)
        t.right(90)
    else:
        for _ in range(10):
            t.forward(20)
            t.color(random.choice(rgb_colors))
            t.dot()
            
        t.left(90)
        t.forward(20)
        t.left(90)



screen.exitonclick()