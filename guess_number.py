import random

# Generate a random number between 1 and 50
number = random.randint(1, 50)
attempts = 0

print("Guess the Number (1–50)")

guess = 0
while guess != number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Correct! You guessed it right {attempts} attempts.")
