# import colorgram
import random
from turtle import Turtle, Screen


# color_p = colorgram.extract('Hirst Spot Painting.jpeg', 15)
ted = Turtle()
ted.pensize(15)
ted.shape("turtle")
ted.color("AntiqueWhite")
ted.pencolor("black")
ted.speed(30)
screen = Screen()
screen.colormode(255)
screen.title("Hirst Painting")
rgb_colors = [(223, 227, 231), (233, 238, 236), (10, 25, 39), (238, 232, 223), (59, 98, 114), (237, 228, 234),
              (137, 162, 184), (32, 11, 6), (158, 76, 36), (199, 156, 121), (42, 9, 23), (7, 38, 17),
              (199, 136, 161), (207, 163, 17), (240, 206, 92)]

ted.penup()
ted.setposition(-335, 320)
y_coordinate = 320


def dot_printer():
    for _ in range(0, 18):
        ted.pendown()
        ted.pencolor(random.choice(rgb_colors))
        ted.forward(0.50)
        ted.penup()
        ted.forward(35)
        ted.pendown()
        ted.forward(0.50)


def set_pos(y_cord, num_lines):
    y_cord_dif = 320 / num_lines
    new_y_pos = y_cord - y_cord_dif
    return new_y_pos, y_cord_dif


for _ in range(0, 20):
    dot_printer()
    ted.penup()
    ted.setposition(-335, set_pos(y_cord=y_coordinate, num_lines=10)[0])
    y_coordinate -= set_pos(y_cord=y_coordinate, num_lines=10)[1]


# for color in color_p:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)

screen.exitonclick()
screen.bye()
