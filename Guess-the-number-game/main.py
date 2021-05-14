from art import logo
import random
from replit import clear

guess_easy = 10
guess_hard = 5


def check_guess(guess, actual_number, chances):
    if guess > actual_number:
        print("Wrong Guess actual number is smaller \n")
        return chances - 1
    elif guess < actual_number:
        print("wrong guess actual answer is Bigger \n")
        return chances - 1
    else:
        print(f"{guess} is the answer! You won \n")


def set_difficulty():
    difficulty = input("You Want this Game to be Hard or Easy?\nType 'easy' or 'hard' ")
    difficulty = difficulty.lower()
    if difficulty == 'easy':
        return guess_easy
    elif difficulty == 'hard':
        return guess_hard
    else:
        print("wrong input!")
        set_difficulty()


def game():
    print(logo)
    print("You have to guess the correct Number\n")
    chances = set_difficulty()
    actual_number = random.randint(1, 101)
    guess = 0
    while guess != actual_number:
        print(f"You have {chances} of Lives \n")
        guess = int(input("Enter the number you want to guess "))
        chances = check_guess(guess, actual_number, chances)
        if chances == 0:
            print("you ran out of lives! you loose! ")
        elif guess != actual_number:
            print("Guess again ")

#testing_git
game()