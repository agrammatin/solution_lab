"""" Draw smile with library turtle
"""
import turtle


# Draw painted circle
def circle_build(radius, color):
    turtle.begin_fill()
    for i in range(120):
        turtle.forward(radius)
        turtle.left(3)
    turtle.color(color)
    turtle.end_fill()
    turtle.color('black')


# Moving turtle and unseen trace
def run_unseen(x_mod, y_mod):
    turtle.penup()
    turtle.goto(x_mod, y_mod)
    turtle.pendown()


# Init turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)

# Draw yellow circle
circle_build(4, 'yellow')
run_unseen(-100, 40)

# Draw first blue circle
circle_build(0.6, 'blue')
run_unseen(-30, 40)

# Draw second blue circle
circle_build(0.6, 'blue')
run_unseen(-76.4, 15)

# Draw nose
turtle.width(6)
turtle.goto(-76.4, -15)

# Draw mouth
run_unseen(-27, -10)
turtle.color('red')
turtle.width(8)
for j in range(60):
    turtle.forward(-2.5)
    turtle.right(3)

turtle.hideturtle()
x = input()
