from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.abe = []
        self.create_snake()
        self.head = self.abe[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        snake_body = Turtle("square")
        snake_body.color("white")
        snake_body.penup()
        snake_body.goto(position)
        self.abe.append(snake_body)

    def reset(self):
        for seg in self.abe:
            seg.goto(1000,1000)
        self.abe.clear()
        self.create_snake()

    def extend(self):
        self.add_segment(self.abe[-1].position())

    def move(self):
        for square in range(len(self.abe) - 1, 0, -1):
            new_x = self.abe[square - 1].xcor()
            new_y = self.abe[square - 1].ycor()
            self.abe[square].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
