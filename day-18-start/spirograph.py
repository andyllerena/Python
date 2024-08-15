from turtle import Turtle,Screen
import random

turtle = Turtle()

Screen().colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r , g ,b)
    return color

turtle.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        current_heading = turtle.heading()
        turtle.setheading(current_heading + 10)


draw_spirograph(3)





screen = Screen()
screen.exitonclick()