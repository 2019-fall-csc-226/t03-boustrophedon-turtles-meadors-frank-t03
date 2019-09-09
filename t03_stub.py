#################################################################################
# Author: Bryar Frank
#           Alex Meadors
# Username: AlexMeadors
#               Frankb
#
# Assignment: T03: Boustrophedon Turtles and Functions
# Purpose:
#################################################################################
# Acknowledgements:
#
#
#################################################################################

import turtle
wn = turtle.Screen()
wn.bgcolor('black')

meadors = turtle.Turtle()
meadors.color('deep sky blue')
meadors.pensize(20)
#meadors.penup()

def square_turtle(name, x, y, size):
    """
    Docstring for function_1
    """

    name.penup()
    name.goto(x, y)
    name.pendown()
    name.setheading(0)
    for side in range(4):
        name.forward(size)
        name.left(90)

    # ...


def squiggle_right(name, x, y):
    """
    Docstring for function_2
    """
    name.goto(x, y)
    name.setheading(90)
    name.pencolor('green')
    for yeeee in range(12):
        name.forward(20)
        name.right(90)
        name.forward(20)
        name.right(90)
        name.forward(20)
        name.left(90)
        name.forward(20)
        name.left(90)
    # ...

def squiggle_left():
    """
    Docstring for function_2
    """
    pass
    # ...

def main():
    """
    Docstring for main
    """
    # ...


square_turtle(meadors, -260, -260, 520)
squiggle_right(meadors, -240, -240)
wn.exitonclick()
