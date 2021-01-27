import random

DECK_SIZE = 5
deck = random.sample(range(1, 13), DECK_SIZE) + [None]

for card,next_card in zip(deck[:-1],deck[1:]):
    if next_card == None: 
        print("You won")
        break2

    correct_guess = "h" if next_card > card else "l"
    guess = input("card is {card} is next h or l? ".format(card=card))

    if guess != correct_guess:
        print("You lost, card was {next_card}".format(next_card=next_card))
        break
