from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", align="center", font=("arial", 30, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", align="center", font=("arial", 30, "normal"))
