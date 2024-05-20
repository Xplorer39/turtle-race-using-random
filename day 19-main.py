import random
import turtle
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

# ALLOWS TO USE WASD TO MOVE AROUND
# def move_forwards():
#     tim.forward(10)
# def move_backwards():
#     tim.backward(10)
# def move_left():
#     tim.left(10)
#     tim.forward(10)
# def move_right():
#     tim.right(10)
#     tim.forward(10)
# screen.onkey(key="c", fun=screen.resetscreen)
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=move_right)


# TURTLE RACE
is_race_on = False
user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win? Enter a color from rainbow:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"YOU WON, THE {winning_color} WON! ")
            else:
                print(f"YOU LOST. {winning_color} WON.")



        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.listen()

screen.exitonclick()
