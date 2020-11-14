"""" Draw with library turtle spider
"""
import turtle
import math


def circle_bild_l(n):
    for i in range(120):
        turtle.forward(n / 3 + 3)
        turtle.left(3)


def circle_bild_r(n):
    for i in range(120):
        turtle.forward(n / 3 + 3)
        turtle.right(3)


turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for j in range(10):
    circle_bild_l(j)
    circle_bild_r(j)


turtle.hideturtle()
x = input()
