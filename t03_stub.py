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
meadors.pensize(25)
#meadors.penup()

def square_turtle(x, y, size):
    """
    Docstring for function_1
    """

    meadors.penup()
    meadors.goto(x, y)
    meadors.pendown()
    meadors.setheading(0)
    for side in range(4):
        meadors.forward(size)
        meadors.left(90)

    # ...


def squiggle_right():
    """
    Docstring for function_2
    """
    for cross_space in range(12):
        meadors.forward(20)
        meadors.right(90)
        meadors.forward(20)
        meadors.right(90)
        meadors.forward(20)
        meadors.left(90)
        meadors.forward(20)
        meadors.left(90)
    # ...

def squiggle_left():
    """
    Docstring for function_2
    """
    for cross_space in range(12):
        meadors.left(90)
        meadors.forward(20)
        meadors.left(90)
        meadors.forward(20)
        meadors.right(90)
        meadors.forward(20)
        meadors.right(90)
        meadors.forward(20)
    # ...

def main():
    """
    Docstring for main
    """
    meadors.speed(0)
    square_turtle(-260, -260, 500)
    meadors.penup()
    meadors.pencolor('green')
    meadors.goto(-240, -240)
    meadors.pendown()
    meadors.setheading(90)
    for fill in range(4):
        squiggle_right()
        meadors.forward(100)
        squiggle_left()
        meadors.forward(20)
    # ...

main()
wn.exitonclick()
