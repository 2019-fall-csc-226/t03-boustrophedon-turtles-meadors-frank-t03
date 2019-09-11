#################################################################################
# Author: Bryar Frank
#           Alex Meadors
# Username: AlexMeadors
#               Frankb
#
# Assignment: T03: Boustrophedon Turtles and Functions
# Purpose: To create a square and fill it in with boustrophedon patterns
#################################################################################
# Acknowledgements:
#
#
#################################################################################
# Import turtle library and create a turtle
#################################################################################
import turtle


#################################################################################
# define functions to create a square using
#################################################################################
def square_turtle(name, x, y, size):
    """
    Creates a square of defined size.
    """
    name.penup()
    name.goto(x, y)
    name.pendown()
    name.setheading(0)
    for side in range(4):
        name.forward(size)
        name.left(90)




def squiggle_right(meadors):
    """
    Uses turtle to fill a line left to right
    """
    for cross_space in range(12):
        for first_arc in range(2):
            meadors.forward(20)
            meadors.right(90)
        for second_arc in range(2):
            meadors.forward(20)
            meadors.left(90)



def squiggle_left(t):
    """
    Uses Turtle to fill a line from right to left
    """
    for cross_space in range(12):
        for first_arc in range(2):
            t.left(90)
            t.forward(20)
        for second_arc in range(2):
            t.right(90)
            t.forward(20)
    # ...


def main():
    """
    Function Starts all the other functions
    Makes and fills a square
    """
    wn = turtle.Screen()
    wn.bgcolor('black')

    meadors = turtle.Turtle()
    meadors.color('deep sky blue')
    meadors.pensize(20)
    meadors.speed(0)

    # Call function to make square and size it
    square_turtle(meadors, -260, -260, 520)

    # move turtle to fill start point
    meadors.penup()
    meadors.pencolor('green')
    meadors.goto(-240, -240)
    meadors.pendown()
    meadors.setheading(90)

    # call both squiggle functions to fill in area
    for fill in range(6):
        squiggle_right(meadors)
        meadors.forward(60)
        squiggle_left(meadors)
        meadors.forward(20)
    # ...

    # fill in last remaining line
    meadors.right(90)
    meadors.forward(480)

    wn.exitonclick()


############################################################################
# set up the screen and turtle, then let the main function do its things
############################################################################
main()


