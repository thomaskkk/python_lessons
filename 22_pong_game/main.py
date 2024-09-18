from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup (width=850, height=650)
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.up, "u")
screen.onkey(r_paddle.down, "e")
screen.onkey(l_paddle.up, "f")
screen.onkey(l_paddle.down, "s")

ball = Ball()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect colision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() 

    # Detect colision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
    elif  ball.distance(l_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    # Detect when paddle misses
    # Right
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset()
    
    # Left
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()

screen.exitonclick()