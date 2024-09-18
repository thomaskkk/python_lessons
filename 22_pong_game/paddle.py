from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, starting_position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(starting_position)

    def up(self):
        if not self.ycor() > 250:
            self.forward(20)

    def down(self):
        if not self.ycor() < -250:
            self.back(20)