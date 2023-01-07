import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
print(cards) #print out with the array syntax

for card in cards:
    print(card)