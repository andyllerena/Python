from turtle import Turtle,Screen

timmy_the_turtle = Turtle()
# timmy_the_turtle.shape('turtle')
# timmy_the_turtle.color(0,1,0)

# Script to make square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# Drawing dashed line
# for _ in range(50):
#     timmy_the_turtle.forward(7)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(7)
#     timmy_the_turtle.pendown()


for _ in range(3):
    timmy_the_turtle.color(1,0,0)
    timmy_the_turtle.right(120)
    timmy_the_turtle.forward(100)

for _ in range(4):
    timmy_the_turtle.color(0,1,0)
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

for _ in range(5):
    timmy_the_turtle.color(0,0,1)
    timmy_the_turtle.right(72)
    timmy_the_turtle.forward(100)













screen = Screen()
screen.exitonclick()