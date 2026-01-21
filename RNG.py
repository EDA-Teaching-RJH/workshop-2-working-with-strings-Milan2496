#random number generator

import random

secret_number = random.randint(1,  10)

user_number = int(input("Guess the randomly generated number"))

if user_number == secret_number:
    print("You have guessed the correct number")
elif user_number > secret_number:
    print("Too high")
else:
    print("Too low")   

