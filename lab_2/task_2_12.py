"""" Draw spring with library turtle
"""
import turtle


def arc(n):
    for i in range(60):
        turtle.forward(n)
        turtle.right(3)


turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for j in range(9):
    if j % 2 == 0:
        arc(2)
    else:
        arc(0.5)

turtle.hideturtle()
x = input()
