from turtle import Turtle

SCORE_FONT = ("Courier", 38, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def partition(self):
        self.goto(0, -250)
        self.setheading(90)
        while self.ycor() < 250:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.penup()

    def update_score(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.l_score, align="center", font=SCORE_FONT)
        self.goto(100, 180)
        self.write(self.r_score, align="center", font=SCORE_FONT)
        self.partition()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()
