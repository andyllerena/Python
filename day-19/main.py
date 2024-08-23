from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_fowards():
    tim.forward(50)

def move_backwards():
    tim.backward(50)

def move_counter_clockwise():
    tim.left(50)

def move_clockwise():
    tim.right(50)

def clear_drawing():
    screen.clearscreen()

screen.listen()
screen.onkey(key='w',fun=move_fowards)
screen.onkey(key='s',fun=move_backwards)
screen.onkey(key='a',fun=move_counter_clockwise)
screen.onkey(key='d',fun=move_clockwise)
screen.onkey(key='c',fun=clear_drawing)

screen.exitonclick()