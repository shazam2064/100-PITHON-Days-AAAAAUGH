import turtle as t
from turtle import Screen
import random

shitle = t.Turtle()

# t.colormode(255)


# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
shitle.pensize(15)
shitle.speed("fastest")

for _ in range(2000):
    shitle.color(random.choice(colors))
    # shitle.color(random_color())
    shitle.forward(30)
    shitle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
