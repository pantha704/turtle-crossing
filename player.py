from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.died_turtle = Turtle()
        self.died_turtle.hideturtle()
        self.died_turtle.color("white")

        self.penup()
        self.go_to_start()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)

    def movee(self):
        self.fd(10)

    def backk(self):
        self.back(10)

    def game_over(self):
        self.died_turtle.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_the_finish_line(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
