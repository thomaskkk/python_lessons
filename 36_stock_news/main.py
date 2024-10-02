import requests
import datetime as dt
from twilio.rest import Client


STOCK = "TSLA" # stock symbol
COMPANY_NAME = "Tesla Inc" # company name
ALPHAVANTAGE_API_URL = "https://www.alphavantage.co/query"
ALPHAVANTAGE_API_KEY = "" # your alphavantage api key here
NEWSAPI_API_KEY = ""  # your newsapi api key here
NEWSAPI_API_URL = "https://newsapi.org/v2/everything"
TWILIO_ACC_ID = ""  # your twilio account id here
TWILIO_AUTH_TOKEN = ""  # your twilio auth token here


alphavantage_paramters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API_KEY,

}

newsapi_paramters = {
    "q": COMPANY_NAME,
    "pageSize": 3,
    "apiKey": NEWSAPI_API_KEY,
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

def stock_diff():
    r = requests.get(ALPHAVANTAGE_API_URL, params=alphavantage_paramters)
    r.raise_for_status()
    data = r.json()
    yesterday = (dt.datetime.now() - dt.timedelta(1)).strftime('%Y-%m-%d')
    day_before = (dt.datetime.now() - dt.timedelta(2)).strftime('%Y-%m-%d')
    yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_close = float(data["Time Series (Daily)"][day_before]["4. close"])
    diff = int(((yesterday_close*100) / day_before_close) - 100) 
    if diff <= -5 or diff >= 5:
        return diff
    else:
        return False

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def last_news():
    r = requests.get(NEWSAPI_API_URL, params=newsapi_paramters)
    r.raise_for_status()
    data = r.json()
    return data["articles"]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

diff = stock_diff()
if diff:
    if diff < 0:
        diff = f"🔻{str(diff*(-1))}%"
    else:
        diff = f"🔺{str(diff)}%"

    client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)
    news = last_news()
    for new in news:
        message_body = f"{STOCK}: {diff}\nHeadline: {new["title"]}\nBrief: {new["description"]}"
        message = client.messages.create(
            from_="whatsapp:REDACTED",
            body=message_body,
            to="whatsapp:REDACTED"
        )