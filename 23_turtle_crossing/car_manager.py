from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.y_pos = random.randrange(-240, 240, 20)
            new_car.goto(280,  new_car.y_pos)
            self.all_cars.append(new_car)


    def move_left(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed  += MOVE_INCREMENT
