#This file will need to use the DataManager,FlightSearch, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

IATA_DEPARTURE_CITY = "LON"
CURRENCY = "GBP"
CURRENCY_SYMBOL = "P"
DAYS_TO_SEARCH = 5

flight_search = FlightSearch()
data_manager = DataManager()
destinations = data_manager.get_destinations()

for destination in destinations:
    if destination["iataCode"] == "":
        iata_code = flight_search.find_city_iata(destination["city"])
        destination["iataCode"] = iata_code 
        data_manager.update_cities_iata(destination["id"], iata_code)

    lowest_flight = flight_search.find_lowest_flight(
        IATA_DEPARTURE_CITY,
        destination["iataCode"],
        CURRENCY,
        destination["lowestPrice"],
        DAYS_TO_SEARCH
    )
    if lowest_flight == None:
        print("No good offers on direct flights found, searching non-direct flights.")
        lowest_flight = flight_search.find_lowest_flight(
            IATA_DEPARTURE_CITY,
            destination["iataCode"],
            CURRENCY,
            destination["lowestPrice"],
            DAYS_TO_SEARCH,
            is_direct=False
        )

if lowest_flight != None:
    recipients = data_manager.get_email_recipients()
    notification = NotificationManager(lowest_flight, CURRENCY_SYMBOL)
    #notification.send_whatsapp()
    notification.send_email(recipients, CURRENCY)
else:
    print("No flight offers found.")
