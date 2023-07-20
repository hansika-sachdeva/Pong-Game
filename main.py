from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-370, 0))
right_paddle = Paddle((370, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.up, "W")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(left_paddle.down, "S")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")


game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # collision with top and bottom walls
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    # collision with right paddle
    if (ball.distance(right_paddle) <= 50 and ball.xcor() > 345) and ball.x_move > 0:
        ball.bounce_x()

    # collision with left paddle
    if (ball.distance(left_paddle) <= 50 and ball.xcor() < -345) and ball.x_move < 0:
        ball.bounce_x()

    # right paddle misses
    if ball.xcor() > 400:
        ball.reset()
        scoreboard.l_point()

    # left paddle misses
    if ball.xcor() < -400:
        ball.reset()
        scoreboard.r_point()


screen.exitonclick()
