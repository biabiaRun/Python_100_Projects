from turtle import Turtle, Screen
import random

tim = Turtle()
tim.screen.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r,g,b)
    return color

def draw_circles(n_circles):
    for i in range(n_circles):
        tim.circle(100)
        tim.left(360/n_circles)
        tim.color(random_color())

draw_circles(100)



# tim.shape("turtle")
# # colors = ["dark red", "dark blue", "dark green","pink","yellow"]
#
# tim.screen.colormode(255)
# direction = [0, 90, 180, 270]
# tim.pensize(7)
# tim.speed(5)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r,g,b)
#     return color
#
# def random_walk():
#     for n in range(200):
#
#         tim.forward(20)
#         angel = random.choice(direction)
#         # color = random.choice(colors)
#         tim.setheading(angel)
#         tim.color(random_color())
#
# random_walk()


# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()