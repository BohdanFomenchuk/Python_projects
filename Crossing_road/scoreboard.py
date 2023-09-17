from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level:{self.score}", align="center", font=("Courier", 15, "normal"))

    def score_add(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over', align="center", font=("Courier", 20, "normal"))
