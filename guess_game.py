# Number Guessing Game
# I built this to practice loops, conditions, and interaction with user

import random

print("Welcome to the Number Guessing Game! ")
print("I am thinking of a number between 1 and 100.")

# generate random number
secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number!")

# bonus: give encouragement
if attempts < 5:
    print("Wow! You are a natural 😎")
elif attempts < 10:
    print("Good job! Keep practicing 💪")
else:
    print("Don't worry, practice makes perfect! 👍")