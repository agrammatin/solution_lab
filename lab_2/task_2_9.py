"""" Draw with library turtle spider
"""
import turtle
import math


def polygon_bild(n):
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

    polygon_bild(j)


turtle.hideturtle()
x = input()
