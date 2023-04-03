from turtle import Turtle
from random import choice
import random

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_VECTOR = choice([UP, DOWN, RIGHT])
colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "LightSeaGreen", "Wheat", "SlateGray", "SeaGreen"]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.last_input = STARTING_VECTOR

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        # new_segment.color(random.choice(colors))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.reset()

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        self.last_input = False
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.move_segment(seg_num)
        self.segments[0].forward(MOVE_DISTANCE)
        self.last_input = self.head.heading()

    def up(self):
        if self.last_input != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.last_input != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.last_input != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.last_input != RIGHT:
            self.head.setheading(LEFT)

    def move_segment(self, seg_num):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
