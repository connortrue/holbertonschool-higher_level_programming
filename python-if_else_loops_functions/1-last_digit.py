#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Get the last digit of the number
if number >= 0:
    last = number % 10
else:
    last = abs(number) % 10 * -1

# Construct the output string based on the last digit
if last > 5:
    print(f"Last digit of {number} is {last} and is greater than 5")
elif last == 0:
    print(f"Last digit of {number} is {last} and is 0")
elif last < 6:
    print(f"Last digit of {number} is {last} and is less than 6 and not 0")
else:
    print(f"boi you messed up")
