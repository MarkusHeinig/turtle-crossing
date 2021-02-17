from turtle import Turtle

FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-260, 260)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def level_up(self):
        self.level += 1

    def game_over(self):
        # self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
