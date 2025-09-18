import time
import random

print("Please guess any number from 1 to 100")
time.sleep(5)


secret_number = random.randint(1, 100)
attempts = 0 

while True:
    guess = input("Enter your guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1  

    if guess < 1 or guess > 100:
        print("Your guess must be between 1 and 100.")
        continue

    if guess == secret_number:
        print(f"Congratulations! You guessed the correct number in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("Too low! Try guessing higher.")
    else:
        print("Too high! Try guessing lower.")
