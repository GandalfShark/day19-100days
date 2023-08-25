"""
Turtle race app from day 19 100 days of python
make a Turtle Race game where you guess the winner
"""
from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('black') 

race_on = False
user_guess = screen.textinput(title="Which turtle do you think will win?",
                              prompt="pick a color: purple, blue, orange, red, yellow, pink.")
user_guess = user_guess.strip().lower()

place = -100
col = 0
# counters for color and place used for generating turtles

turtle_names = ('don', 'leo', 'mike', 'raph', 'tommy', 'tim')
colors = ['purple', 'blue', 'orange', 'red', 'yellow', 'pink']

all_turtles = []
for t in turtle_names:
    t = Turtle(shape="turtle")
    t.penup()
    t.goto(x=-230, y=place)
    place += 50
    t.color(colors[col])
    col += 1
    all_turtles.append(t)
    # create turtles, and make a list of all the turtle object locations

if user_guess:
    race_on = True

while race_on:
    for turt in all_turtles:
        if turt.xcor() >= 230:
            race_on = False
            winning_turtle = turt.pencolor()

            print(f'The winning turtle was {winning_turtle} color. You guessed {user_guess}.')

            if winning_turtle == user_guess:
                print('YOU WIN!!')
            elif winning_turtle != user_guess:
                print('Better luck next time.')

        distance_traveled = random.randint(0, 10)
        turt.forward(distance_traveled)

screen.exitonclick()
