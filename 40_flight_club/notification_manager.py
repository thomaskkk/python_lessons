from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib
from email.message import EmailMessage

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data: dict, currency_symbol: str) -> None:
        load_dotenv()
        self.currency_symbol = currency_symbol
        self.trip_cost = flight_data["price"]["grandTotal"]
        self.departure_iata = flight_data["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        self.destination_iata = flight_data["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
        self.trip_date = flight_data["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
        self.direct_flight = True
        
        if len(flight_data["itineraries"][0]["segments"]) > 1:
            self.direct_flight = False
            self.arrivals_list = [iata_code for iata_code in ["itineraries"][0]["segments"][:-1]]

        self.twilio_sid = os.getenv("TWILIO_SID")
        self.twilio_token = os.getenv("TWILIO_TOKEN")
        self.whatsapp_sender = os.getenv("WHATSAPP_SENDER")
        self.whatsapp_receiver = os.getenv("WHATSAPP_RECEIVER")
        self.email_sender = os.getenv("EMAIL_SENDER")
        self.email_pass = os.getenv("EMAIL_PASS")
        
    def send_whatsapp(self):
        """Call Twillio API and send a whatsapp message from the sender number to the receiver numeber"""
        client = Client(username=self.twilio_sid, password=self.twilio_token)
        message_body = f"Low price alert! Only {self.currency_symbol} {self.trip_cost} to fly from {self.departure_iata} to {self.destination_iata}, on {self.trip_date}"
        print(f"Sending whatsapp msg to {self.whatsapp_receiver}: {message_body}")
        client.messages.create(
            from_=f"whatsapp:{self.whatsapp_sender}",
            body=message_body,
            to=f"whatsapp:{self.whatsapp_receiver}"
        )
    def send_email(self, recipients: dict, currency: str):
        if not self.direct_flight:
            message_body = f"Low price alert! Only {currency} {self.trip_cost} to fly from {self.departure_iata} to {self.destination_iata}, on {self.trip_date}, stops at {self.arrivals_list}"
        else:
            message_body = f"Low price alert! Only {currency} {self.trip_cost} to fly from {self.departure_iata} to {self.destination_iata}, on {self.trip_date}"

        for recipient in recipients:
            message = EmailMessage()
            message.set_content(message_body)
            message['Subject'] = "Low price alert!"
            message['From'] = self.email_sender
            message['To'] = recipient["whatIsYourEMail?"]
            
            smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            smtp.login(self.email_sender, self.email_pass)
            smtp.send_message(message)
            print(f"email sent to: {recipient["whatIsYourEMail?"]}")

