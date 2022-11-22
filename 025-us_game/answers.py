from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 8, 'normal')

class Answers(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def update_answers(self, state, x, y):
        self.goto(x, y)
        self.write(state, align=ALIGNMENT, font=FONT)
