from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.color("red")
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0,-30)
        self.write(f"Your Score Is {self.score}", align=ALIGNMENT, font=FONT)


