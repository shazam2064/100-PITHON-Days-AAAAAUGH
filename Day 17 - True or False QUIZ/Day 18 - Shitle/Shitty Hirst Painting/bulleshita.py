import turtle as t
import random

t.colormode(255)
shitle = t.Turtle()

shitle.speed("fastest")
shitle.penup()
shitle.hideturtle()

color_list = [(237, 230, 96), (13, 115, 170), (166, 79, 46), (188, 12, 63), (213, 157, 87), (129, 181, 203),
              (234, 76, 46),
              (33, 139, 83), (5, 34, 91), (146, 167, 35), (76, 40, 21), (110, 187, 165), (167, 47, 91), (227, 117, 147),
              (14, 170, 212), (59, 160, 89), (6, 95, 51), (219, 71, 119), (95, 21, 69), (240, 162, 190),
              (147, 205, 224),
              (12, 87, 106), (211, 222, 10), (248, 170, 145), (9, 45, 127), (7, 75, 41)]

shitle.setheading(220)
shitle.forward(300)
shitle.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    shitle.dot(31, random.choice(color_list))
    shitle.forward(50)

    if dot_count % 10 == 0:
        shitle.setheading(90)
        shitle.forward(50)
        shitle.setheading(180)
        shitle.forward(500)
        shitle.setheading(0)

screen = t.Screen()
screen.exitonclick()
