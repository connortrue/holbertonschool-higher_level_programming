#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
last_digit = number % 10

# Construct the output string based on the last digit
if last_digit > 5:
    output = f"Last digit of {number} is {last_digit} and is greater than 5\n"
elif last_digit == 0:
    output = f"Last digit of {number} is {last_digit} and is 0\n"
else:
    output = f"Last digit of {number} is {last_digit} and is less than 6 and not 0\n"

# Print the final output
print(output)
