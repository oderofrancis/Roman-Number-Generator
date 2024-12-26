"""
Step 1: Set up Twilio

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

# Twilio credentials
TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")    # Replace with your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = f"whatsapp:{config("TWILIO_WHATSAPP_NUMBER")}"  # Twilio's WhatsApp sandbox number
TO_WHATSAPP_NUMBER =  f"whatsapp:{config("TO_WHATSAPP_NUMBER")}"  # The recipient's WhatsApp number

# Function to generate random numbers
def generate_random_numbers():
    three_digit = random.randint(100, 999)
    four_digit = random.randint(1000, 9999)
    five_digit = random.randint(10000, 99999)
    six_digit = random.randint(100000, 999999)
    return three_digit, four_digit, five_digit, six_digit

# Function to send the WhatsApp message
def send_whatsapp_message():
    random_numbers = generate_random_numbers()
    number_labels = ["Three-digit", "Four-digit", "Five-digit", "Six-digit"]
    message_body = "Random numbers generated:\n" + "\n".join(
        f"{label}: {number}" for label, number in zip(number_labels, random_numbers)
    )
    
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN) # Initialize Twilio client
    
    # Send the WhatsApp message
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )
    
    print(f"Message sent: {message.sid}")

for period in ["18:45","18:46","18:47"]:
    schedule.every().day.at(period).do(send_whatsapp_message)

    print(f"Scheduler is running. Waiting for {period} AM...")
    while True:
        schedule.run_pending()
        time.sleep(1)
