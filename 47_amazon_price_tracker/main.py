import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

URL = "https://www.amazon.com.br/Stand-100x22Cm-Suporte-elevado-Monitor/dp/B0CWJHWK2T"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
}

r = requests.get(URL, headers=headers)
r.raise_for_status()

soup = BeautifulSoup(r.text, "html.parser")
price = soup.find("span", class_="a-price-whole").getText()
price += soup.find("span", class_="a-price-fraction").getText()
if "," in price:
    price = price.replace(",", ".") 
price = float(price)

BUY_PRICE = 200

if price < BUY_PRICE:
    load_dotenv()

    product = soup.find(id="productTitle").get_text().strip()
    message_body = f"The product {product} that you're watching is now a low value of {price}\n{URL}"

    message = EmailMessage()
    message.set_content(message_body)
    message['Subject'] = "Low price alert!"
    message['From'] = os.getenv("SENDER_EMAIL")
    message['To'] = os.getenv("SENDER_EMAIL")

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(os.getenv("SENDER_EMAIL"), os.getenv("SENDER_PASS"))
    smtp.send_message(message)
    print(f"email sent to: {os.getenv("SENDER_EMAIL")}")
