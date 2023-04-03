import turtle as t
from turtle import Screen
import random

shitle = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]

shitle.penup()
shitle.left(90)
shitle.forward(500)
shitle.left(90)
shitle.forward(50)
shitle.right(180)
shitle.pendown()


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        shitle.forward(10)
        shitle.right(angle)


for shape_side_n in range(3, 361):
    # shitle.color(random.choice(colors))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()
