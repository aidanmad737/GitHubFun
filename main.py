import random
from player import Player
from deck import Deck

'''From Cards i think that it should include 
init Deck
shuffle deck
list of cards

Each card should also provide 
value comparisons

From Player i think that it should include
init player
name
Actions: draw card, collect cards, check if player has cards
'''

#Main
def main():
    print("Welcome to Two-Deck War!")
#I think that somoene also should create an init function to create the Deck
    deck1 = Deck()
    deck2 = Deck()
 #shuffle the decks to randomize the order of the cards
    deck1.shuffle()
    deck2.shuffle()

    player1 = Player("Player 1", deck1.cards)
    player2 = Player("Player 2", deck2.cards)
 #Battle of the decks
 #draw card function should be pretty straightforward, 
 #I think it should remove the top card from the player's deck and return it.
    while player1.has_cards() and player2.has_cards():
        card1 = player1.draw_card()
        card2 = player2.draw_card()

        print(f"{player1.name} drew the {card1}.")
        print(f"{player2.name} drew the {card2}.")

        cards_played = [card1, card2]

        while card1.value == card2.value:
            print("War!")

            if not player1.has_cards():
                print(f"{player1.name} ran out of cards for war!")
                break
            if not player2.has_cards():
                print(f"{player2.name} ran out of cards for war!")
                break

            card1 = player1.draw_card()
            card2 = player2.draw_card()

            print(f"{player1.name} drew the {card1}.")
            print(f"{player2.name} drew the {card2}.")

            cards_played.append(card1)
            cards_played.append(card2)
        #I'm thinking that collect_cards can be used to add the cards played in the round to the winner's deck. 
        #This way, the winner of the round will have more cards to play in future rounds.
        random.shuffle(cards_played)
        if card1.value > card2.value or not player2.has_cards():
            print(f"{player1.name} wins the round!")
            player1.collect_cards(cards_played)
        else:
            print(f"{player2.name} wins the round!")
            player2.collect_cards(cards_played)
        #For above^^ I'm not sure how you guys want to determine card value, I googled this .value cmd.
        #feel free to change it to whatever you guys want. I just think the card values should be compared
        print(f"Cards in {player1.name}'s deck: {len(player1.cards)}")
        print(f"Cards in {player2.name}'s deck: {len(player2.cards)}")
        input("Press Enter to play the next round.")

    if player1.has_cards():
        print(f"{player1.name} wins the game!")
    else:
        print(f"{player2.name} wins the game!")


main()