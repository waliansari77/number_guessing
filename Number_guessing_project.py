from art import logo
import random as rnd
print(logo)

random_number = rnd.randint(1,100)

def check_answer(user_guess):
    global random_number
    if user_guess > random_number:
        print("Too high")
        print("Guess again")
    elif user_guess < random_number:
        print("Too low")
        print("Guess again")

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

level = input("Choose a difficulty. type 'easy' or hard: ").lower()
max_attempts = 0
if level == "easy":
    max_attempts = 10
elif level == "hard":
    max_attempts = 5
else:
    print("You have to choose a difficulty.")

attempts = 0

while attempts < max_attempts:
    print(f"You have {max_attempts} attempts remaining to guess the number.")
    max_attempts -= 1
    user_guess = int(input("Make a guess: "))

    if user_guess == random_number:
        print(f"You got it! the answer was {user_guess}")
        attempts = max_attempts
    elif attempts >= max_attempts:
        print("You have run out of guesses, you lose.")
    else:
        check_answer(user_guess)
