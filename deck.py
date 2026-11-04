import random
from cards import Card
#making the class

class Deck:
    def __init__(self):
        suits = ["Spades","Hearts","Clubs","Diamonds"]#suits and ranks
        ranks = ["2","3","4","5","6","7","8","9","10","Jack", "Queen", "King", "Ace"]

        self.cards = []

        for suit in suits:
            value = 2
#assigning values so we know who will win
            for rank in ranks:
                self.cards.append(Card(suit, rank, value))
                value += 1
#shuffle function
    def shuffle(self):
        random.shuffle(self.cards)
