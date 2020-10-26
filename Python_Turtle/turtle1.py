# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary scri"""

import turtle
my_wn=turtle.Screen()
for i in range(30):
    turtle.circle(5*i)
    turtle.circle(-5*i)
    turtle.left(i)
turtle.exitonclick()