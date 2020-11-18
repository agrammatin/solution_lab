"""" Draw num post index track smile with library
"""
import turtle
import sys
from random import randint

max_step = 700
turtle.setup(max_step, max_step)
turtle.Screen().tracer(2)
number_of_turtles = 20
steps_of_time_number = 500

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

speed = dict()
for unit in pool:
    unit.penup()
    unit.speed(0)
    unit.setpos(randint(-300, 300), randint(-300, 300))
    unit.right(randint(-180, 180))
    speed[unit] = randint(1, 10)

for i in range(steps_of_time_number):
    for unit in pool:
        # Mirror for right
        if unit.xcor() + speed[unit] > (max_step / 2) - 15:
            delta = (max_step / 2) - unit.xcor() - 15
            unit.forward(delta)
            if unit.heading() < 90:
                unit.right(180 + 2 * unit.heading())
            else:
                unit.right(unit.heading() - 180 - (360 - unit.heading()))
            unit.forward(speed[unit] + delta + 1)
        # Mirror for left
        elif unit.xcor() - speed[unit] < -(max_step / 2) + 15:
            delta = (max_step / 2) + unit.xcor() - 15
            unit.forward(delta)
            if unit.heading() < 180:
                angel = 180 - unit.heading()
                unit.left(180 + 2 * angel)
            else:
                angel = unit.heading() - 180
                unit.left(180 - 2 * angel)
            unit.forward(speed[unit] + delta + 1)

        # Mirror for top
        elif unit.ycor() + speed[unit] > (max_step / 2) - 15:
            delta = (max_step / 2) - unit.ycor() - 15
            unit.forward(delta)
            if unit.heading() < 90:
                unit.right(180 - 2 * (90 - unit.heading()))
            else:
                unit.right(180 - 2 * (90 - unit.heading()))
            unit.forward(speed[unit] + delta + 1)
        # Mirror for bottom
        elif unit.ycor() - speed[unit] < -(max_step / 2) + 15:
            delta = (max_step / 2) + unit.ycor() - 15
            unit.forward(delta)
            if unit.heading() < 270:
                unit.left(180 + 2 * (270 - unit.heading()))
            else:
                unit.left(180 - 2 * (unit.heading() - 270))
            unit.forward(speed[unit] + delta + 1)
        else:
            unit.forward(speed[unit])
x = input()
