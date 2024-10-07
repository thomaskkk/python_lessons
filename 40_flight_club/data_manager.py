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
        self.sheety_price_sheet = os.getenv("SHEETY_PRICE_SHEET")
        self.sheety_user_sheet = os.getenv("SHEETY_USER_SHEET")
        self.sheet_auth = (os.getenv("SHEETY_AUTH_USER"), os.getenv("SHEETY_AUTH_PASS"))

    def get_destinations(self) -> dict:
        """
        Call Sheety API and return the lines of the spreadshet containing the country, iana code and max price.

        Returns:
            dict: A json cotaining each row of the sheet.
        """
        r = requests.get(
                url=f"{self.api_url}/{self.sheety_user}/{self.sheety_project}/{self.sheety_price_sheet}",
                auth=self.sheet_auth
            )
        r.raise_for_status()
        return r.json()["prices"]

    def update_cities_iata(self, destination_id: int, iata_code: str) -> None:
        """
        Call Sheety API and updates the city iata code on the mentioned destination_id.

        Args:
            destination_id (int): the id of the row to update.
            iata_code (str): the value of the IATA city code to update in the cell.
        """
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }

        r = requests.put(
            url=f"{self.api_url}/{self.sheety_user}/{self.sheety_project}/{self.sheety_price_sheet}/{destination_id}",
            auth=self.sheet_auth,
            json=params
        )
        r.raise_for_status()

    def get_email_recipients(self) -> dict:
        """
        Call Sheety API to get all users that signup to receive email alerts

        Returns:
            dict: A json cotaining each row (signup_user) of the sheet.
        """

        r = requests.get(
            url=f"{self.api_url}/{self.sheety_user}/{self.sheety_project}/{self.sheety_user_sheet}",
            auth=self.sheet_auth
        )
        r.raise_for_status()
        return r.json()["users"]