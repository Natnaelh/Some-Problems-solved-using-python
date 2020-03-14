#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:14:51 2020

@author: natnem
"""

import turtle
myturtle = turtle.Turtle()
mywin = turtle.Screen()


def snowflakeedge(length , order):
    if order == 0 :
        myturtle.forward(length)
        
    else:
        
        length /= 3
        snowflakeedge(length , order - 1)
        myturtle.left(60)
        
        snowflakeedge(length , order - 1)
        myturtle.right(120)
        
        snowflakeedge(length , order - 1)
        myturtle.left(60)
        
        snowflakeedge(length , order - 1)
        
def snowflake(order):
    myturtle.color("green")
    snowflakeedge(100,order)
    myturtle.right(90)
    myturtle.color("yellow")
    snowflakeedge(300 , order)
    myturtle.right(90)
    myturtle.color("red")
    snowflakeedge(100 , order)
    myturtle.right(90)
    myturtle.color("red")
    snowflakeedge(300 , order)
    
    

myturtle.pensize(3)
snowflake(3)
mywin.exitonclick()




