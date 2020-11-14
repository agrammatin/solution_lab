"""" Draw with library turtle spider
"""
import turtle
import math


def circle_bild_l():
    for i in range(120):
        turtle.forward(3)
        turtle.left(3)


def circle_bild_r():
    for i in range(120):
        turtle.forward(3)
        turtle.right(3)


turtle.shape('turtle')
turtle.speed(0)

for j in range(3):

    circle_bild_l()
    circle_bild_r()
    turtle.left(60)


turtle.hideturtle()
x = input()
