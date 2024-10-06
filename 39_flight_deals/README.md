# Flight deals

This is a tracker that monitors flight prices and send an alert when a flight is lower.


This challenge teaches the concepts of:

 - HTTP API requests
 - HTTP Auth (oauth2)
 - OOP

## Setup

This program uses the Python requests, dotenv, oauthlib.oauth2, requests_oauthlib, twilio

```
pip install requests python-dotenv oauthlib requests_oauthlib twilio
```

Rename .env_sample to .env and fill with your credentials from [Sheety](https://sheety.co/), [Amadeus](https://developers.amadeus.com/) and [Twilio](https://www.twilio.com/en-us)

## How to run

```
python main.py
```