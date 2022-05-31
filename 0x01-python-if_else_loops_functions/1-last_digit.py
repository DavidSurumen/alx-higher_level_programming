#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = int(str(number)[-1])
print(f"Last digit of {number} is {last_digit} and is", end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("zero")
else:
    print("less than 6 and not 0")
