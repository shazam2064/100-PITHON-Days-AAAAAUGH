from turtle import Turtle, Screen

shitle = Turtle()

for _ in range(15):
    shitle.forward(10)
    shitle.penup()
    shitle.forward(10)
    shitle.pendown()

screen = Screen()
screen.exitonclick()
