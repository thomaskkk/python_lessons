##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import datetime as dt
import pandas
import random
import os
import smtplib
from email.message import EmailMessage

EMAIL_SENDER = "" #add email here
EMAIL_PASS = "" #add app password here
EMAIL_SUBJECT = "Happy birthday!"

def generate_letter(recipient):
    random_letter = random.choice(os.listdir("letter_templates"))
    with open (f"letter_templates/{random_letter}") as data_file:
        template = data_file.read()
        letter = template.replace("[NAME]", recipient)
    
    return letter

def send_letter(to_email, letter):
    message = EmailMessage()
    message.set_content(letter)
    message['Subject'] = EMAIL_SUBJECT
    message['From'] = EMAIL_SENDER
    message['To'] = to_email
    
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL_SENDER, EMAIL_PASS)
    smtp.send_message(message)

now = dt.datetime.now()
df = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for index, row in df.iterrows()}

if (now.month, now.day) in birthdays_dict:
    name = birthdays_dict[(now.month, now.day)]["name"]
    email = birthdays_dict[(now.month, now.day)]["email"]
    letter = generate_letter(name)
    send_letter(email, letter)
