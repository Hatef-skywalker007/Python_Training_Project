import random

number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Guess: "))

    if guess == 0:
        print("Game over!")
        break

    attempts += 1

    if guess == number:
        print("🎉 You won!")
        print("Attempts:", attempts)
        break

    elif guess < number:
        print("Go higher!")

    else:
        print("Go lower!")