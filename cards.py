import random
from deck import Deck

#Card Class
class Card:
#Creates card attributes
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

#Retunrs card name
    def __str__(self):
        return f"{self.rank} of {self.suit}"