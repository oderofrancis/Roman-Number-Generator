import random

def generate_random_numbers():
    three_digit = random.randint(100, 999)
    four_digit = random.randint(1000, 9999)
    five_digit = random.randint(10000, 99999)
    six_digit = random.randint(100000, 999999)
    
    return three_digit, four_digit, five_digit, six_digit

random_numbers = generate_random_numbers()

number_labels = ["Three-digit", "Four-digit", "Five-digit", "Six-digit"]
# for number in random_numbers:
#     print(number)