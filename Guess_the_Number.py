import random

number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == number:
        print("🎉 Correct!")
        print(f"Attempts: {attempts}")
        break

    elif guess < number:
        print("Too low!")

    else:
        print("Too high!")