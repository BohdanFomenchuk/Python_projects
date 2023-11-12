
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
colors = ['green', 'yellow', 'red', 'blue', 'black', 'orange']
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? Enter a color: ')

turtles = []

position = 105

for i in range(0, 6):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(-230, position)
    position -= 35
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle the winner")
            else:
                print(f"You've lost. The {winning_color} turtle the winner")
        else:
            r_distance = random.randint(0, 10)
            turtle.forward(r_distance)


screen.exitonclick()
