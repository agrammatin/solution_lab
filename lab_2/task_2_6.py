"""" Draw with library turtle spider
"""
import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range(12):
    turtle.rt(30 * i)
    turtle.fd(100)
    turtle.stamp()
    turtle.home()

turtle.hideturtle()
x = input()
