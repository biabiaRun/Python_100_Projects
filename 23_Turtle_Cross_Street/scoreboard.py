from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="left", font=FONT)

    def game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER. \nYou score is {self.score}", align="center", font=FONT)


