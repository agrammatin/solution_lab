"""" Draw num post index track smile with library
"""
import turtle


def draw_0(x_pos):
    turtle.goto(x_pos, -100)
    turtle.goto(x_pos + 50, -100)
    turtle.goto(x_pos + 50, 0)
    turtle.goto(x_pos, 0)
    turtle.penup()
    turtle.goto(x_pos + 100, 0)
    turtle.pendown()


def draw_1(x_pos=0):
    turtle.penup()
    turtle.goto(x_pos, -50)
    turtle.pendown()
    turtle.goto(x_pos + 50, 0)
    turtle.goto(x_pos + 50, -100)
    turtle.penup()
    turtle.goto(x_pos + 50, 0)
    turtle.goto(x_pos + 100, 0)
    turtle.pendown()


def draw_4(x_pos):
    turtle.goto(x_pos, -50)
    turtle.goto(x_pos + 50, -50)
    turtle.goto(x_pos + 50, -100)
    turtle.goto(x_pos + 50, 0)
    turtle.penup()
    turtle.goto(x_pos + 100, 0)
    turtle.pendown()


def draw_7(x_pos):
    turtle.goto(x_pos + 50, 0)
    turtle.goto(x_pos, -50)
    turtle.goto(x_pos, -100)
    turtle.penup()
    turtle.goto(x_pos, 0)
    turtle.goto(x_pos + 100, 0)
    turtle.pendown()


turtle.shape('turtle')
turtle.speed(1)

turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(135)
turtle.pendown()
turtle.forward(((50 ** 2) * 2) ** 0.5)
turtle.right(135)
turtle.forward(100)
turtle.left(180)
turtle.penup()
turtle.forward(100)
turtle.right(90)
turtle.forward(50)
'''
turtle.penup()
x_st = -300
turtle.goto(x_st, 0)
turtle.pendown()
draw_1(x_st + 0)
draw_4(x_st + 100)
draw_1(x_st + 200)
draw_7(x_st + 300)
draw_0(x_st + 400)
draw_0(x_st + 500)
'''

# turtle.hideturtle()
x = input()
