from turtle import Turtle

# PADDLE_WIDTH = 20
# PADDLE_HEIGHT = 100
MOVE_DISTANCE = 30
# each up and down command moves the paddle by 30 pixels


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        if self.ycor() < 200:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -200:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)
