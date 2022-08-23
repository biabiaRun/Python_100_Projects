import time
from turtle import Turtle, Screen
import random
import time

# screen = Screen()
# tim = Turtle()
# ''' Proj 1- Draw anything controled by keyboard and home in the end'''
# def fwd():
#     tim.forward(10)
#
# def bwd():
#     tim.backward(10)
#
# def ccw():
#     tim.right(5)
#
# def cw():
#     tim.left(5)
# def clr():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# tim.screen.listen()
# tim.screen.onkey(fun=fwd, key="w")
# tim.screen.onkey(fun=bwd, key="s")
# tim.screen.onkey(fun=ccw, key="a")
# tim.screen.onkey(fun=cw, key="d")
# tim.screen.onkey(fun=clr, key="c")


'''Proj-2 Turtle race'''
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Turtle Race", prompt="Which turtle will win the race: "
                                                        "red,green,yellow,black,orange,purple\n"
                                                        "Choose the color you bet: ")
print(user_bet)
colors = ["red","green","yellow","black","orange","purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []
if user_bet:
    move_on = True

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.speed("slow")
    new_turtle.goto(x=-220, y=y_position[i])
    all_turtles.append(new_turtle)

while move_on:
    '''Below is my code, which works. But second versin from teacher is better'''
    # for i in range(6):
    #     random_dist = random.randint(0, 10)
    #     all_turtles[i].forward(random_dist)
    #     if all_turtles[i].xcor() > 200:
    #         winner = all_turtles[i].color()[0]
    #         if winner == user_bet:
    #             print("YOU WIN :)")
    #         else:
    #             print(f"YOU LOSE :( The winner is {winner}")
    #         move_on = False

    for turtle in all_turtles:
        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)
        if turtle.xcor() > 200:
            move_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print("YAYA, YOU WIN!")
            else:
                print(f"Sorry you lost. The winner is {winner}")









# t_r.penup()
# t_r.goto(x=-200,y=-50)
# t_r.color("red")
#
#
# t_b.penup()
# t_b.goto(x=-200,y=0)
# t_b.color("blue")
#
# t_g.penup()
# t_g.goto(x=-200,y=50)
# t_g.color("green")
#
#
# def race():
#     while t_r.pos()[0] < 200 and t_b.pos()[0] < 200 and t_g.pos()[0] < 200:
#         t_r.speed(random.choice(a))
#         print(t_r.speed(random.choice(a)))
#         t_r.penup()
#         t_r.forward(5)
#
#         t_b.speed(random.choice(a))
#         t_b.speed(random.choice(a))
#         t_b.penup()
#         t_b.forward(5)
#
#
#         t_g.speed(random.choice(a))
#         t_g.speed(random.choice(a))
#         t_g.penup()
#         t_g.forward(5)
#
#         print("=======\n")
#         time.sleep(0.5)
#         if t_r.pos()[0] == 199:
#             screen.textinput(title="Race", prompt="Red is winner!")
#             print('Red is winner!')
#             time.sleep(0.5)
#         elif t_g.pos()[0] == 199:
#             screen.textinput(title="Race", prompt="Green is winner!")
#             print('Green is winner!')
#             time.sleep(0.5)
#         elif t_b.pos()[0] == 199:
#             screen.textinput(title="Race", prompt="Blue is winner!")
#             print('Blue is winner!')
#
# race()




screen.exitonclick()
