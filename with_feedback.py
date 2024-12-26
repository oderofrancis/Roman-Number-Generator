import random
from twilio.rest import Client
import schedule
import time
from decouple import config

# Twilio credentials
TWILIO_ACCOUNT_SID = config("TWILIO_ACCOUNT_SID")  # Replace with your Twilio Account SID
TWILIO_AUTH_TOKEN = config("TWILIO_AUTH_TOKEN")    # Replace with your Twilio Auth Token
TWILIO_WHATSAPP_NUMBER = f"whatsapp:{config('TWILIO_WHATSAPP_NUMBER')}"  # Twilio's WhatsApp sandbox number
TO_WHATSAPP_NUMBER = f"whatsapp:{config('TO_WHATSAPP_NUMBER')}"  # The recipient's WhatsApp number

# Function to generate random numbers
def generate_random_numbers():
    three_digit = random.randint(100, 999)
    four_digit = random.randint(1000, 9999)
    five_digit = random.randint(10000, 99999)
    six_digit = random.randint(100000, 999999)
    return three_digit, four_digit, five_digit, six_digit

# Function to convert numbers to Roman numerals
def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syms[i]
            num -= val[i]
        i += 1
    return roman_num

# Function to send the WhatsApp message
def send_whatsapp_message():
    random_numbers = generate_random_numbers()
    roman_numbers = [int_to_roman(num) for num in random_numbers]
    message_body = (
        "Random numbers generated (convert to Roman numerals):\n" +
        "\n".join(
            f"{label}: {num}" for label, num in zip(
                ["Three-digit", "Four-digit", "Five-digit", "Six-digit"], random_numbers
            )
        )
    )

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)  # Initialize Twilio client

    # Send the WhatsApp message
    message = client.messages.create(
        body=message_body,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=TO_WHATSAPP_NUMBER
    )
    print(f"Message sent: {message.sid}")

    # Simulate receiving a user response (replace this with Twilio webhook integration in production)
    user_response = input("Enter your Roman numeral response (comma-separated): ")
    user_answers = user_response.split(",")
    correct_answers = all(
        user_answer.strip().upper() == correct_roman
        for user_answer, correct_roman in zip(user_answers, roman_numbers)
    )

    if correct_answers:
        client.messages.create(
            body="Congratulations! You answered correctly. You have won!",
            from_=TWILIO_WHATSAPP_NUMBER,
            to=TO_WHATSAPP_NUMBER
        )
        print("Correct answers confirmed. Follow-up message sent.")

for period in ["18:52"]:#,"18:46","18:47"]:
    schedule.every().day.at(period).do(send_whatsapp_message)

    print(f"Scheduler is running. Waiting for {period} AM...")
    while True:
        schedule.run_pending()
        time.sleep(1)