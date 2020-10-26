# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 15:49:32 2020

@author: srish
"""

import turtle

BODY_COLOR='purple'

BODY_SHADOW=''
GLASS_COLOR='#9acedc'
GLASS_SHADOW=''


t=turtle.Turtle()

def body():
    t.pensize(20)
    t.speed(9)
    
    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40,-180)
    t.right(180)
    t.forward(200)
        
        # head curve
    t.right(180)
    t.circle(100,-180)
        
        #left side
    t.backward(20)
    t.left(15)
    t.circle(500,-20)
    t.backward(20)
        
        #t.backwards(200)
    t.circle(40,-180)
    #t.right(90)
    t.left(7)
    t.backward(50)
        #hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    #t.right(180)
    #t.circle(25,-180)
    t.right(240)
    t.circle(50,-70)
    t.end_fill()
    
def glass():
    t.up()
    #t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()
    
    t.right(150)
    t.circle(90,-55)
    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)
    #t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)
    t.right(180)
    t.circle(45,-30)
    t.end_fill()
 #or body color   
def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)
   
    t.fillcolor(BODY_COLOR)
    
    t.begin_fill()
    
    t.down()
    t.forward(30)
    t.right(255)
    
    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()

    

body()
glass()
backpack()

t.screen.exitonclick()

    
        
    