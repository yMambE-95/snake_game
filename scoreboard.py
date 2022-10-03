from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data_high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_scoring()

    def update_scoring(self):
        self.clear()
        self.write(f"Score: {self.score} high score  {self.high_score} ", align=ALIGNMENT, font=FONT)

    def scoring(self):
        self.score += 1
        self.update_scoring()

    def restart_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data_high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoring()

