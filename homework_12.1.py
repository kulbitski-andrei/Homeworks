"""HOMEWORK 12.1: CARDS"""

import random


class CardDeckClass:
    """Simple and nice deckbuilder for home usage.
    Creates a new deck exemplar on initialization.
    Can shuffle deck and return chosen card to a user"""

    def __init__(self):

        self.deck_list = []
        self.number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                            "Jack", "Queen", "King", "Ace", "Joker"]
        self.mast_list = ["Diamonds", "Hearts", "Clubs", "Spades"]

        for number in self.number_list:
            for mast in self.mast_list:
                self.deck_list.append(number + " of " + mast)

    def deck_shuffle(self):
        """Shuffles the deck by randomizing elements in the list"""

        random.shuffle(self.deck_list)

    def deck_get(self, index_number):
        """Returns card by its sequence number, provided by the user"""

        return self.deck_list[index_number]


card_deck_exemplar = CardDeckClass()
card_deck_exemplar.deck_shuffle()
card_selected = int(input("There are 56 cards in the deck. "
                          "Select the sequence number of the card "
                          "you want to reveal... ")) - 1
card = card_deck_exemplar.deck_get(card_selected)
print(f"The card you have chosen is a {card}")
