from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "bold")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 280)
        self.score = 0
        self.retrieve_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def add_point(self):
        self.score  += 1
        self.update_scoreboard()

    def store_high_score(self, score):
        with open("high_score.txt", mode="w") as file:
            file.write(str(self.high_score))

    def retrieve_high_score(self):
        try:
            with open("high_score.txt") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            print("High score file does not exists, creating a new file...")
            self.high_score = 0
            with open("high_score.txt", mode="w") as file:
                file.write(str(self.high_score))
        


