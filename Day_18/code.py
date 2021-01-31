from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141),
              (254, 194, 0)]
timmy_the_turtle.penup()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.hideturtle()
y_axis = -200
timmy_the_turtle.setx(-200)
timmy_the_turtle.sety(y_axis)
# timmy_the_turtle.pendown()
screen.colormode(255)

for _ in range(10):

    for _ in range(10):
        timmy_the_turtle.dot(20, random.choice(color_list))
        timmy_the_turtle.penup()
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.setx(-200)
    y_axis += 50
    timmy_the_turtle.sety(y_axis)
    timmy_the_turtle.setheading(0)


screen.exitonclick()