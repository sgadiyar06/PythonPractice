# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 22:18:21 2020

@author: Sudarshan
"""



# Python program to draw  
# Rainbow Benzene 
# using Turtle Programming 
import turtle 
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 
t = turtle.Pen() 
turtle.bgcolor('black') 
for x in range(360): 
    t.pencolor(colors[x%6]) 
    t.width(x/100 + 1) 
    t.forward(x) 
    t.left(59) 