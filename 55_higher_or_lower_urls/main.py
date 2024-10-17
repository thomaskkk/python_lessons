from flask import Flask
import random

app = Flask(__name__)

number = random.randrange(0, 9)

@app.route("/")
def home():
    return f'<h1>Guess a number between 0 and 9</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">{number}'

@app.route("/<int:guess>")
def check_number(guess):
    if guess == number:
        return '<h1>You got it!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmxoZzd3dWEwY2o5MWVkcmFvbHhhb3R5YmhiYjRybDE0M2ZkNWludiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26FPLMDDN5fJCir0A/giphy.gif">'
    elif guess > number:
        return '<h1>Too high!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXp3amVzZmxtNWt4OGtlNzhueWV3dXNsYTd1a2NndDNzd2t5a3BtNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3XrAfHxRxropW/giphy.gif">'
    elif guess < number:
        return '<h1>Too low!</h1><img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWVwaXFlNjRteWVic3kxN2FwMXQ3ZGM3bTloZHpiODV2bzZwYjEzciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3NtY188QaxDdC/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)