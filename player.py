#Player Class
#Represents one person in the game. Each player holds their own pile of Card objects.
#The front of the list (index 0) is the top of the pile, and the end of the list is the bottom.
class Player:
    #Each player has a name and their own pile of cards
    #cards is a list of Card objects (it comes from that player's Deck)
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    #Removes the top card from the player's pile and returns it
    #pop(0) takes the card at the front of the list, so the pile gets one card smaller
    def draw_card(self):
        return self.cards.pop(0)

    #Adds the cards won in a round to the bottom of the player's pile
    #extend adds every card in cards_won to the end of the list
    def collect_cards(self, cards_won):
        self.cards.extend(cards_won)

    #True if the player still has at least one card
    #main.py uses this to know when the game is over and when a player can't continue a war
    def has_cards(self):
        return len(self.cards) > 0

    #How many cards the player has
    def card_count(self):
        return len(self.cards)

    #Lets us print a player directly, e.g. print(player1) -> "Player 1 (52 cards)"
    def __str__(self):
        return f"{self.name} ({self.card_count()} cards)"