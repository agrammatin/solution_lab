"""" Draw spider with library turtle
"""
import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range(12):
    turtle.rt(30)
    turtle.fd(100)
    turtle.stamp()
    # turtle.home()
    turtle.rt(180)
    turtle.fd(100)
    turtle.rt(180)

turtle.hideturtle()
x = input()
