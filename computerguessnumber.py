import time

print("Think of a number between 1 and 100, and I will try to guess it.")
time.sleep(5)

low = 1
high = 100
attempts = 0

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is {guess}.")
    feedback = input("Is it correct, higher, or lower? ").lower()

    if feedback == "correct":
        print(f"Yay! I guessed your number in {attempts} attempts.")
        break
    elif feedback == "higher":
        low = guess + 1
    elif feedback == "lower":
        high = guess - 1
    else:
        print("Please respond with 'correct', 'higher', or 'lower'.")
    
    if low > high:
        print("Hmm, something doesn't add up. Are you sure you gave the right hints?")
        break
