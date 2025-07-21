import random

secret_number = random.randint(1, 10)
guess = None
attempts = 0

while guess != secret_number and attempts < 5:
    guess = int(input("Guess the number (1-10): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("You got it!")

if guess != secret_number:
    print("Sorry, you're out of attempts. The number was", secret_number)