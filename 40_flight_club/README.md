# Flight club

This is an update to flight tracker program now providing flight offers to multiple users via e-mail.


This challenge teaches the concepts of:

 - HTTP API requests
 - HTTP Auth (oauth2)
 - OOP

## Setup

This program uses the Python requests, dotenv, oauthlib.oauth2, requests_oauthlib, twilio

```
pip install -r requirements.txt
```
or

```
pip install requests python-dotenv oauthlib requests_oauthlib twilio
```

Rename .env_sample to .env and fill with your credentials from [Sheety](https://sheety.co/), [Amadeus](https://developers.amadeus.com/) and [Twilio](https://www.twilio.com/en-us)

## How to run

```
python main.py
```