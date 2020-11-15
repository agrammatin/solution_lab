"""" Draw flower with library turtle
"""
import turtle


def circle_build_l():
    for i in range(120):
        turtle.forward(3)
        turtle.left(3)


def circle_build_r():
    for i in range(120):
        turtle.forward(3)
        turtle.right(3)


turtle.shape('turtle')
turtle.speed(0)

for j in range(3):

    circle_build_l()
    circle_build_r()
    turtle.left(60)


turtle.hideturtle()
x = input()
