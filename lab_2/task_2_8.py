"""" Draw square spiral with library turtle
"""
import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range(40):
    turtle.fd(5 + i * 5)
    turtle.lt(90)

turtle.hideturtle()
x = input()
