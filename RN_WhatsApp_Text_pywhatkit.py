import random
import pywhatkit as kit
import datetime
from decouple import config

kit.start_server()

def generate_random_numbers():
    three_digit = random.randint(100, 999)
    four_digit = random.randint(1000, 9999)
    five_digit = random.randint(10000, 99999)
    six_digit = random.randint(100000, 999999)
    
    return three_digit, four_digit, five_digit, six_digit

def send_whatsapp_message():
    # Generate random numbers
    random_numbers = generate_random_numbers()
    
    # Prepare message
    message = (
        "Random numbers generated:\n"
        f"Three-digit: {random_numbers[0]}\n"
        f"Four-digit: {random_numbers[1]}\n"
        f"Five-digit: {random_numbers[2]}\n"
        f"Six-digit: {random_numbers[3]}"
    )
    
    # Set target number and time
    phone_number = config("TO_WHATSAPP_NUMBER")  # Replace with the actual number
    time_hour = 18  # example : 7 AM
    time_minute = 35  # 30 minutes past the hour
    
    # Send the message
    kit.sendwhatmsg(phone_number, message, time_hour, time_minute)

# Schedule the message
current_time = datetime.datetime.now()
if current_time.hour == 17 and current_time.minute == 35:
    send_whatsapp_message()
