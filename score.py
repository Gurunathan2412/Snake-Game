from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.hideturtle()
        self.write(f"Score: {self.value}", True, align="center", font=("Arial", 15, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", True, align="center", font=("Arial", 20, "bold"))

    def increase(self):
        self.value += 1
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.value}", True, align="center", font=("Arial", 15, "bold"))

