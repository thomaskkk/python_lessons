import requests
from dotenv import load_dotenv
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import datetime as dt
import time

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        load_dotenv()
        self.amadeus_api_key = os.getenv("AMADEUS_API_KEY")
        self.amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
        self.amadeus_api_url = "https://test.api.amadeus.com"
        self.session = self.get_token()

    def get_token(self):
        client = BackendApplicationClient(client_id=self.amadeus_api_key)
        oauth = OAuth2Session(client=client)
        oauth.fetch_token(
            token_url=f"{self.amadeus_api_url}/v1/security/oauth2/token",
            client_id=self.amadeus_api_key, 
            client_secret=self.amadeus_api_secret
        )
        return oauth
    
    def find_city_iata(self, city: str):
        """
        Call the Amadeus API and returns an IATA code of the city given part of the city name.

        Args:
            city (str): Complete or partial string of the city name to seach for.

        Returns:
            str: IANA city code or None.
        """
        params = {
            "keyword": city,
        }
        r = self.session.get(url=f"{self.amadeus_api_url}/v1/reference-data/locations/cities", params=params)
        r.raise_for_status()
        if r.json()["meta"]["count"] > 0:
            return r.json()["data"][0]["iataCode"]
        else:
            return None
        
    def find_flight_offer(self, iana_departure: str, iana_destination: str, departure_date: str, currency: str, max_price: int, is_direct: bool=True) -> (dict | None):
        """
        Call the Amadeus API an find offers given the departure, destination, currency and looking for offers lower
        than max_price.

        Args:
            iana_departure (str): iana code of the city to search for departure flights.
            iana_destination (str): iana code of the city to search for destination flights.
            departure_date (str): date of departure in YYY-mm-dd format.
            currency (str): currency code ex.: BRL, USD or EUR.
            max_price (int): seach will look for offers lower than this price.
            is_direct(bool): if True only search for direct flights.

        Returns:
            dict: dictionary of the offers on depature date or None.
        """
        result = None
        params = {
            "originLocationCode": iana_departure,
            "destinationLocationCode": iana_destination,
            "departureDate": departure_date,
            "adults": 1,
            "currencyCode": currency,
            "maxPrice": max_price,
            "nonStop": "true" if is_direct else "false",
        }
        r = self.session.get(url=f"{self.amadeus_api_url}/v2/shopping/flight-offers", params=params)
        r.raise_for_status()
        result = r.json()
        
        return result
    
    def find_lowest_flight(self, iana_departure: str, iana_destination: str, currency: str, max_price: int, days_to_search: int, is_direct: bool=True) -> (dict | None):
        """
        From a series of calls on find_flight_offer on Amadeus API find the lowest one given a start price and number of
        days to search from.

        Args:
            iana_departure (str): iana code of the city to search for departure flights.
            iana_destination (str): iana code of the city to search for destination flights.
            currency (str): currency code ex.: BRL, USD or EUR.
            max_price (int): value to start search from, offers should be lower than this value.
            days_to_search (int): number of days to keep searching for offers ex.: 30 days starting from tomorrow.
            is_direct(bool): if True only search for direct flights.

        Returns:
            dict: returns the dict of the best offer or None.
        """
        lowest_price = max_price
        best_offer = None
        current_date = dt.datetime.today() + dt.timedelta(days=1)
        end_date = current_date + dt.timedelta(days=days_to_search)
        delta = dt.timedelta(days=1)
        while current_date <= end_date:
            result = self.find_flight_offer(
                iana_departure=iana_departure,
                iana_destination=iana_destination,
                departure_date=current_date.strftime("%Y-%m-%d"),
                currency=currency,
                max_price=lowest_price,
                is_direct="true" if is_direct else "false",
            )
            if result["meta"]["count"] > 0:
                for entry in result["data"]:
                    if int(float(entry["price"]["grandTotal"])) < lowest_price:
                        lowest_price = int(float(entry["price"]["grandTotal"]))
                        best_offer = entry
                        print(f"New lowest price: {lowest_price} {currency}")
            time.sleep(2)
            print(f"Searching offers for: {iana_destination} on {current_date.strftime("%Y-%m-%d")}")
            current_date += delta

        return best_offer

