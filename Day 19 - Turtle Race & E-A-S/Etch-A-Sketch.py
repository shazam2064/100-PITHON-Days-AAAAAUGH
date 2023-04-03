from turtle import Turtle, Screen

shitle = Turtle()
screen = Screen()


def move_forwards():
    shitle.forward(30)


def move_backwards():
    shitle.backward(30)


def turn_left():
    new_heading = shitle.heading() + 30
    shitle.setheading(new_heading)


def turn_right():
    new_heading = shitle.heading() - 30
    shitle.setheading(new_heading)


def clear():
    shitle.clear()
    shitle.penup()
    shitle.home()
    shitle.pendown()


screen.listen()
screen.onkey(move_forwards, "Up")
screen.onkey(move_backwards, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(clear, "c")

screen.exitonclick()
