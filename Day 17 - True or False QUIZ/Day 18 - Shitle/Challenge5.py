import turtle as t
from turtle import Screen
import random

shitle = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


shitle.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        shitle.color(random_color())
        shitle.circle(100)
        shitle.setheading(shitle.heading() + size_of_gap)


draw_spirograph(20)

screen = Screen()
screen.exitonclick()
