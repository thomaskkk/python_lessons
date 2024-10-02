import requests
from dotenv import load_dotenv
import os

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self) -> None:
        load_dotenv()
        self.api_url = "https://api.sheety.co"
        self.sheety_user = os.getenv("SHEETY_USER")
        self.sheety_project = os.getenv("SHEETY_PROJECT")
        self.sheety_sheet = os.getenv("SHEETY_SHEET")
        self.sheet_auth = (os.getenv("SHEETY_AUTH_USER"), os.getenv("SHEETY_AUTH_PASS"))

    def get_destinations(self):
        r = requests.get(
                url=f"{self.api_url}/{self.sheety_user}/{self.sheety_project}/{self.sheety_sheet}",
                auth=self.sheet_auth
            )
        r.raise_for_status()
        return r.json()["prices"]

    def update_cities_iata(self, destination_id: int, iata_code: str):
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }

        r = requests.put(
            url=f"{self.api_url}/{self.sheety_user}/{self.sheety_project}/{self.sheety_sheet}/{destination_id}",
            auth=self.sheet_auth,
            json=params
        )
        r.raise_for_status()        