"""
A simple etch-a-sketch like program with a turtle.
TURTLE SKETCH! now with 100% less real turtles
from day 19 of 100 days of Python
"""

from turtle import Screen, Turtle
# Tim the turtle settings #
tim = Turtle()
tim.shape("turtle")
tim.color("green")
tim.pencolor('orange')

# display settings for window #
display = Screen()
display.bgcolor("black")


# movement functions #
def move_forward():
    tim.forward(10)


def move_backward():
    tim.back(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()
    # clear off all pen lines from tim and send him to start

# the main section of program #
display.listen()
# the instance of screen called display is not going to liten for keystrokes n such
display.onkey(key="s", fun=move_backward)
display.onkey(key="w", fun=move_forward)
display.onkey(key="d", fun=turn_right)
display.onkey(key="a", fun=turn_left)
display.onkey(key="c", fun=clear)
# NOTE: don't use the () when setting up the fun var, because the function is used as na input
# this is called a -- higher order function -- a function that takes functions and does stuff with them
# kwargs are better for this sort of thing
display.exitonclick()
# only close the window when the mouse is clicked
