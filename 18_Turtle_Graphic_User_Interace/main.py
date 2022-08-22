# # import colorgram
# # rgb_color = []
# # colors = colorgram.extract('image.jpg', 9)
# # for item in colors:
# #     r = item.rgb.r
# #     g = item.rgb.g
# #     b = item.rgb.b
# #     new_color = (r,g,b)
# #     rgb_color.append(new_color)
# # print(rgb_color) # GENERATE BELOW LIST
#
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83)]

from turtle import Turtle, Screen
import random

tim = Turtle()
tim.screen.colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 20

for i in range(1,number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.penup()
        tim.setheading(0)


screen = Screen()
screen.exitonclick()

#
# ''' FIGURE OUT THE RANGE() METHOD DIFFERENCE'''
# out = []
# for i in range(5):
#     out.append(i)
# print(out)
#
# out1 = []
# for i in range(0, 5):
#     out1.append(i)
# print(out1)
#
# out2 = []
# for i in range(1,5):
#     out2.append(i)
# print(out2)