import turtle
import random

color_list = [(188, 19, 46), (244, 233, 64), (217, 239, 245), (195, 76, 34), (218, 66, 106), (13, 143, 89),
              (18, 125, 173), (196, 176, 17), (108, 182, 209), (12, 167, 214), (208, 154, 91), (238, 232, 3),
              (25, 40, 75), (36, 43, 111), (78, 175, 96), (181, 44, 65), (217, 67, 47), (217, 129, 153),
              (125, 185, 120), (238, 161, 180), (7, 61, 38), (147, 209, 220), (8, 91, 52), (5, 86, 109), (160, 30, 27),
              (237, 170, 163), (158, 211, 188)]

def go_back():
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    timmy.forward(500)
    timmy.right(180)


timmy = turtle.Turtle()
timmy.shape("circle")
timmy.pensize(20)
timmy.speed("fastest")
turtle.colormode(255)

timmy.screen.screensize(300, 300, "white")
print(timmy.screen.screensize())

timmy.penup()
timmy.hideturtle()
timmy.setpos(-250,-250)


for y in range(10):
    for x in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)
    go_back()



timmy.screen.exitonclick()
