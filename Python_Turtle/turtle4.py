# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 10:42:07 2020

@author: srish
"""


from turtle import Turtle, Screen

def draw_square(some_turtle):

    for i in range (1,5):
        some_turtle.forward(200)
        some_turtle.right(90)

def draw_art():
    window = Screen()
   
    #Turtle Brad
    brad = Turtle(shape="circle")
    brad.color("green")
    brad.speed(6)
    brad.pensize(2)
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)
    #Turtle Angie
    angie = Turtle(shape="circle")
    angie.color("orange")
    angie.speed(5)
    angie.pensize(2)
    size=1
    while (True):
        angie.forward(size)
        angie.right(91)
        size = size + 1

    window.exitonclick()

draw_art()