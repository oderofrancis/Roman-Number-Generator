"""
Set up Twilio

    Sign up for Twilio: https://www.twilio.com/ and create a new account.

    Get a WhatsApp-enabled Twilio number:
        In the Twilio console, enable the "WhatsApp Sandbox."
        Follow the instructions to join the sandbox by sending a code from your WhatsApp.

    Install the Twilio Python library:
        'pip install twilio'


"""

import random
from twilio.rest import Client
import schedule
import time
from decouple import config
from roman_number import random_numbers,number_labels

TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")  # Twilio Account SID
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")    # Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = f"whatsapp:{config("TWILIO_WHATSAPP_NUMBER")}"  # Twilio's WhatsApp sandbox number
TO_WHATSAPP_NUMBER =  f"whatsapp:{config("TO_WHATSAPP_NUMBER")}"  # The recipient's WhatsApp number

# Send the WhatsApp message
def send_whatsapp_message():
    message_body = "Random numbers generated:\n" + "\n".join(
        f"{label}: {number}" for label, number in zip(number_labels, random_numbers)
    )
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # Initialize Twilio client
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )
    # print(f"Message sent: {message.sid}")
for period in ["09:19","09:20","09:21"]:
    schedule.every().day.at(period).do(send_whatsapp_message)

    print(f"Scheduler is running. Waiting for {period}...")
    while True:
        schedule.run_pending()
        time.sleep(1)
