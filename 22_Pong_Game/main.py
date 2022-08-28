from turtle import Turtle,Screen

screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
#paddle.hideturtle()
paddle.penup()
paddle.goto(x=750, y=0)
#paddle.showturtle()
paddle.shapesize(stretch_wid=5, stretch_len=1)



def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(x=paddle.xcor(), y=new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(x=paddle.xcor(), y=new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    Screen().update()




screen.exitonclick()