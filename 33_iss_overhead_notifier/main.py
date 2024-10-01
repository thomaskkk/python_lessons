import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time
from config import *


def iss_in_range():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT + 5 >= iss_latitude and MY_LAT - 5 <= iss_latitude) and (MY_LONG + 5 >= iss_longitude and MY_LONG - 5 <= iss_longitude):
        return True
    else:
        return False

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }


    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    hour_now = datetime.now().hour

    if hour_now > sunset or hour_now < sunrise:
        return True
    else:
        return False
    
def send_email(to_email, body):
    message = EmailMessage()
    message.set_content(body)
    message['Subject'] = EMAIL_SUBJECT
    message['From'] = EMAIL_SENDER
    message['To'] = to_email
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    smtp.send_message(message)
    print("mail sent")


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
run_program = True
while run_program:
    if iss_in_range() and is_night():
        send_email(EMAIL_DESTINATION, EMAIL_BODY)
    time.sleep(60)


