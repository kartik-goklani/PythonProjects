import turtle
from random import choice

rgb_colors = [(202, 166, 109), (150, 73, 49), (222, 202, 139), (167, 151, 45), (54, 93, 123), (133, 33, 24),
              (133, 163, 184), (49, 117, 87), (197, 92, 72), (18, 96, 75), (99, 74, 76),
              (67, 47, 41), (147, 177, 148), (162, 143, 157), (232, 178, 166), (56, 47, 50)]


timmy = turtle.Turtle()

turtle.colormode(255)
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()
timmy.setheading(220)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, choice(rgb_colors))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
screen.exitonclick()
