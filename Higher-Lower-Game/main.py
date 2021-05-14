from replit import clear
from art import logo
from art import vs
from game_data import data
import random

comparision = []


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def comparision_function(guess, details_a, details_b):
    follower_count_a = details_a['follower_count']
    follower_count_b = details_b['follower_count']
    if follower_count_a > follower_count_b:
        return guess == 'a'
    elif follower_count_b > follower_count_a:
        return guess == 'b'


def details(details):
    name = details['name']
    description = details['description']
    country = details['country']
    return (f"{name} a {description} from {country}")


def game():
    score = 0
    print(logo)
    person_a = get_random_account()
    person_b = get_random_account()
    game_is = True
    while game_is:
        person_a = person_b
        person_b = get_random_account()
        while person_a == person_b:
            person_b = get_random_account()

        print(f"Compare A: {details(person_a)}")
        print(vs)
        print(f"Compare B: {details(person_b)} \n")

        guess = input("Who have more followers \n").lower()
        is_correct = comparision_function(guess, person_a, person_b)
        clear()
        if is_correct:
            score += 1
            print("Thats a Correct Answer!\n")
        else:
            print("Wrong Answer! your score is :", score)
            game_is = False


game()