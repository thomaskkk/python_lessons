import requests

API_URL = "https://opentdb.com/api.php"
NUMBER_OF_QUESTIONS = 10
CATEGORY = 15
DIFFICULTY = "medium"
TYPE = "boolean"

parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "category": CATEGORY,
    "difficulty": DIFFICULTY,
    "type": TYPE,
}

response = requests.get(API_URL, params=parameters)
response.raise_for_status()

data = response.json()
question_data = data["results"]
