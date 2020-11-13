"""" Draw with library turtle more square
"""
import turtle

turtle.shape('turtle')
turtle.speed(1)

for i in range(1, 12):
    for j in range(3):
        turtle.fd(i * 10)
        turtle.lt(90)
    turtle.fd(i * 10)
    turtle.hideturtle()
    turtle.speed(0)
    turtle.penup()
    turtle.rt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.fd(5)
    turtle.lt(90)
    turtle.pendown()
    turtle.showturtle()
    turtle.speed(1)

turtle.hideturtle()
x = input()
