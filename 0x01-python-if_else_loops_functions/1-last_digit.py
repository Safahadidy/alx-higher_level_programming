#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_digit = number % 10
else:
    last_digit = -(-number) % 10
s1 = f"Last digit of {number} is {last_digit}"
if last_digit < 6:
    print(f"{s1} and is less than {6} and not {0}")
elif last_digit > 5:
    printf(f"{s1} and is greater than 5")
elif last_digit == 0:
     printf(f"{s1} and is 0")
