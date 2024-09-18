from turtle import Screen, Turtle
from states import States

NUM_OF_STATES = 50
score = 0

screen = Screen()
screen.title("U.S. States Game")
IMAGE = "blank_states_img.gif"
screen.setup(730, 500, 3000)
screen.addshape(IMAGE)

turtle = Turtle()
turtle.shape(IMAGE)

states = States()

game_is_on = True

while game_is_on:
    answer = screen.textinput(title=f"{score}/{NUM_OF_STATES} States Correct",  prompt="What's another state name?")
    if answer == "Exit":
        game_is_on = False
    elif states.guess_state(answer.title()):
        score += 1

