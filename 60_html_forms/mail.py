import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os


class Mail():
    """docstring for Mail."""
    def __init__(self):
        load_dotenv()

        self.sender = os.getenv("SENDER")
        self.recipient = os.getenv("RECIPIENT")
        self.app_password = os.getenv("APP_PASSWORD")


    def send_email(self, subject, body, sender):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = self.recipient
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.app_password)
            smtp_server.sendmail(sender, self.recipient, msg.as_string())