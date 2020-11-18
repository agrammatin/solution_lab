"""" Draw random track smile with library
"""
import turtle
import random

turtle.shape('turtle')
turtle.color('red')
turtle.speed(0)
for i in range(1000):
    turn = random.random()
    if turn > 0.5:
        turtle.right(random.randint(0, 360))
    else:
        turtle.left(random.randint(0, 360))
    turtle.forward(random.randint(0, 50))


turtle.hideturtle()
x = input()
