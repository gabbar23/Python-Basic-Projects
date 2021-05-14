############### Blackjack Project #####################

from replit import clear
import random
from art import logo


def calculator_score(cards):
    sum(cards)

    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        return sum(cards)
    else:
        return sum(cards)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        print("Its a Draw! 🥺\n")

    elif user_score == 0:
        print("Black Jack! You won 💰\n")

    elif dealer_score == 0:
        print("Dealer got a Black Jack! You Lost! ⚰️\n")

    elif user_score > 21:
        print("You Lost! 😭\n")

    elif dealer_score > 21:
        print("You Won! 🤑\n")

    elif user_score > dealer_score:
        print("You Won! 🤑\n")

    elif user_score < dealer_score:
        print("You Lost! 😭\n")


def game_start():
    user = []
    dealer = []
    print(logo)

    def deal_card():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return cards[random.randrange(0, 12)]

    for time in range(2):
        user.append(deal_card())
        dealer.append(deal_card())

    game_end = False
    while not game_end:
        user_score = calculator_score(user)
        dealer_score = calculator_score(dealer)

        print(f"Your First two cards are : {user} and current score :{sum(user)} \n")
        print(f"Computer's First card is : [{dealer[0]}]\n")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_end = True
        else:
            pick = input("Do you want to draw another card? Y or N \n")
            if pick == 'Y':
                print("\n")
                user.append(deal_card())
            elif pick == 'N':
                game_end = True
                while dealer_score != 0 and dealer_score < 17:
                    dealer.append(deal_card())
                    dealer_score = calculator_score(dealer)

    print(f"Final cards of User are : {user} and score :{sum(user)} \n")
    print(f"Final cards of Computer are : {dealer} and score : {sum(dealer)}\n")
    compare(user_score, dealer_score)


while input("Do you want to play a game of Black jack? Y or N ") == "Y":
    clear()
    game_start()





