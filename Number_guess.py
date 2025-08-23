#!/usr/bin/env python3

import random

secret_number = random.randint(1, 20)
print("Guess a number between 1 and 20:")

for guesses_taken in range(6):
    guess = int(input())
    if guess < secret_number:
        print("Your guess is too low.")
    elif guess > secret_number:
        print("Your guess is too high.")
    else:
        break

if guess == secret_number:
    print("Congratulations! You guessed the number.")
else:
    print("Sorry, you didn't guess the number. The secret number was", secret_number)