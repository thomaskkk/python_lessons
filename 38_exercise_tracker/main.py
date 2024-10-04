import requests
from requests.auth import HTTPBasicAuth
import datetime as dt
import os
from dotenv import load_dotenv

load_dotenv()

GENDER = "male"
WEIGHT_KG = 95
HEIGHT_CM = 168
AGE = "46"

API_HOST = "https://trackapi.nutritionix.com"

SHEETY_HOST = "https://api.sheety.co"

headers1     = {
    "x-app-id": os.environ.get("APP_ID"),
    "x-app-key": os.environ.get("API_KEY"),
}

exercise1 = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

endpoint1 = f"{API_HOST}/v2/natural/exercise"
r1 = requests.post(url=endpoint1, headers=headers1, json=exercise1)
r1.raise_for_status()
data = r1.json()

for exercise in data["exercises"]:
    exercise2 = {   
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    endpoint2 = f"{SHEETY_HOST}/{os.environ.get('SHEETY_USERNAME')}/{os.environ.get('SHEETY_PROJECT')}/{os.environ.get('SHEETY_SHEET')}"
    r2 = requests.post(url=endpoint2, json=exercise2, auth=(os.environ.get("SHEETY_AUTH_USER"), os.environ.get("SHEETY_AUTH_PASS")))
    r2.raise_for_status()
    print(r2.text)


