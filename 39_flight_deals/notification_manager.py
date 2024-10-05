class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data: dict, currency_symbol: str) -> None:
        self.currency_symbol = currency_symbol
        self.trip_cost = flight_data["price"]["grandTotal"]
        self.departure_iata = flight_data["itineraries"]["segmenst"]
        self.destination_iata = flight_data
        self.trip_date = flight_data
        
    def send_message(self):
        #client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)
        message_body = f"Low price alert! Only {self.currency_symbol}{self.trip_cost} to fly from {self.departure_iata} to {self.destination_iata}, on {self.trip_date}"
        print(message_body)
        # client.messages.create(
        #     from_="whatsapp:{SENDER}",
        #     body=message_body,
        #     to="whatsapp:{RECEIVER}"
        # )
