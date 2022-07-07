from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)
        self.shape("square")
        self.color("white")

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
