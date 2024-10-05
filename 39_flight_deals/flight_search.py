import requests
from dotenv import load_dotenv
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import datetime as dt

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
        params = {
            "keyword": city,
        }
        r = self.session.get(url=f"{self.amadeus_api_url}/v1/reference-data/locations/cities", params=params)
        r.raise_for_status()
        if r.json()["meta"]["count"] > 0:
            return r.json()["data"][0]["iataCode"]
        else:
            return None
        
    def find_flight_offer(self, iana_departure: str, iana_destination: str, departure_date: str, max_price: int):
        result = None
        params = {
            "originLocationCode": iana_departure,
            "destinationLocationCode": iana_destination,
            "departureDate": departure_date,
            "adults": 1,
            "currencyCode": "BRL",
            "maxPrice": max_price,
        }
        r = self.session.get(url=f"{self.amadeus_api_url}/v2/shopping/flight-offers", params=params)
        r.raise_for_status()
        result = r.json()
        
        return result
    
    def find_lowest_flight(self, iana_departure: str, iana_destination: str, max_price: int):
        lowest_price = max_price
        best_offer = None
        current_date = dt.datetime.today() + dt.timedelta(days=1)
        end_date = current_date + dt.timedelta(days=(30*6))
        delta = dt.timedelta(days=1)
        while current_date <= end_date:
            result = self.find_flight_offer(iana_departure, iana_destination, current_date.strftime("%Y-%m-%d"), lowest_price)
            if result["meta"]["count"] > 0:
                for entry in result["data"]:
                    if int(float(entry["price"]["grandTotal"])) < lowest_price:
                        lowest_price = int(float(entry["price"]["grandTotal"]))
                        best_offer = entry
                        print(f"New lowest price: {lowest_price}"   )
            
            print(f"{iana_destination} - {current_date.strftime("%Y-%m-%d")}")
            current_date += delta

        return best_offer

