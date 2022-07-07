from turtle import Screen, Turtle
from paddle_class import Paddle
from ball_class import Ball
from scoreboard_class import Score
import time

window = Screen()
window.bgcolor("black")
window.setup(width=800, height=600)
window.title("Pong Game")
window.tracer(0)
middle_line = Turtle()
middle_line.color("white")
middle_line.pensize(4)
middle_line.hideturtle()
middle_line.penup()
middle_line.goto(0, -290)
middle_line.setheading(90)
for _ in range(15):
    middle_line.pendown()
    middle_line.forward(20)
    middle_line.penup()
    middle_line.forward(20)
ball = Ball()
right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))
right_score = Score((50, 250))
left_score = Score((-50, 250))

window.listen()
window.onkeypress(right_paddle.move_up, "Up")
window.onkeypress(right_paddle.move_down, "Down")
window.onkeypress(left_paddle.move_up, "w")
window.onkeypress(left_paddle.move_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    window.update()
    ball.move_ball()
    # Detect ball collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # Detect ball collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
    elif ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    # Detect ball collision out of right_paddle
    if ball.xcor() > 400:
        ball.reset_position()
        left_score.increase_score()
    # Detect ball collision out of left_paddle
    if ball.xcor() < -400:
        ball.reset_position()
        right_score.increase_score()
window.mainloop()
