"""" Draw polygon with library turtle
"""
import turtle
import math


def polygon_build(n):
    angle = 360 / n
    turtle.left((180 - angle) / 2)
    for i in range(1, n + 1):
        turtle.left(angle)
        turtle.forward(10 * n * 2 * math.sin(math.pi / n))
    turtle.right((180 - angle) / 2)


turtle.shape('turtle')
turtle.speed(1)

for j in range(3, 14):
    turtle.penup()
    turtle.fd(10)

    turtle.pendown()

    polygon_build(j)


turtle.hideturtle()
x = input()
