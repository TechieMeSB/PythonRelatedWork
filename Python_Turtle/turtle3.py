# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:59:50 2020

@author: srish
"""

import turtle
import random
turtle.speed(speed='fastest')
def draw(n,x,angle):
    for i in range(n):
        turtle.colormode(255)
        a=random.randint(0,255)
        b=random.randint(0,255) #choose random intergers to generate random rgb values
        c=random.randint(0,255)
        
        turtle.pencolor(a,b,c) #set outline
        turtle.fillcolor(a,b,c) #fills color
        
        turtle.begin_fill()
        for j in range(5):
            turtle.forward(5 *n-5*i)
            turtle.right(x)
            turtle.forward(5 *n-5*i)
            turtle.right(72-x)
        turtle.end_fill()
        turtle.rt(angle)
        
n=30
x=144
angle=18
draw(n,x,angle)