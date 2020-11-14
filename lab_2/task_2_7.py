"""" Draw with library turtle spider
"""
import turtle
import math

turtle.shape('turtle')
turtle.speed(1)

for j in range(360 * 2):
    turtle.fd(0.05+0.01*j)
    turtle.lt(5)

turtle.hideturtle()
x = input()
