from turtle import Turtle,Screen
import random

tim = Turtle()

colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "DeepSkyBlue"]
directions = [0,90,180,270]
tim.width(3)
tim.speed(7)

for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(50)
    tim.setheading(random.choice(directions))








screen = Screen()
screen.exitonclick()