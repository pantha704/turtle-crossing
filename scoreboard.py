from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.goto(-170, 260)

    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="right", font=("Arial", 24, "normal"))

