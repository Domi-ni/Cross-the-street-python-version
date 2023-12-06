from turtle import Turtle
FONT = ("Courier", 16, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.hideturtle()
        self.color("black")
        self.penup()
        self.update_scoreboard()

    def score_point(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-235, y=260)
        self.write(arg=f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)






