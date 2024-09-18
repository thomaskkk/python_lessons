from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=650, height=650, startx=2000, starty=500)
screen.screensize(600, 600)
screen.title("Turtle crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.create_car()
    car_manager.move_left()
    screen.update()

    # Detect colision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect reach goal
    if player.ycor() > 280:
        car_manager.level_up()
        scoreboard.level_up()
        player.start()


screen.exitonclick()