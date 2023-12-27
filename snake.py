from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        # setting properties and creating the snake
        self.starting_x = 0
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("#145A32")
        tim.goto(self.starting_x, 0)
        self.starting_x -= MOVE_DISTANCE
        self.segments.append(tim)

    def extend(self):
        tim = Turtle(shape="square")
        tim.penup()
        tim.color("#145A32")
        self.segments.append(tim)

    # implement this

    def move_snake(self):
        # we start with the last element, that the len - 1, and ask it to move to the position of the element in front, and
        # do that for all the subsequent elements in a loop, outside which we move just the first element forward by 20px
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_front = self.segments[seg_num - 1].xcor()
            y_front = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_front, y_front)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270.0:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90.0:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180.0:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0.0:
            self.head.setheading(180)
