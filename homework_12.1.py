"""HOMEWORK 12.1"""

import random


class Card:
    """Provides a storage for list of card numbers (values)
     and card suits """

    number_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                   "Jack", "Queen", "King", "Ace"]
    mast_list = ["Diamonds", "Hearts", "Clubs", "Spades"]

    def __init__(self, number, mast):
        self.number = number
        self.mast = mast


class CardsDeck:
    """Simple and nice deckbuilder for home usage.
    Creates a new deck exemplar on initialization.
    Can shuffle deck and return chosen card to a user"""

    def __init__(self, number_list_from_card, mast_list_from_card):

        self.deck_list = []

        for _number in number_list_from_card:
            for _mast in mast_list_from_card:
                exemplar_card = Card(_number, _mast)
                self.deck_list.append(exemplar_card)
        self.deck_list.append(Card("Joker", "Reds"))
        self.deck_list.append(Card("Joker", "Blacks"))

    def deck_shuffle(self):
        """Shuffles the deck by randomizing elements in the list"""

        random.shuffle(self.deck_list)

    def deck_get(self, index_number):
        """Returns card by its sequence number, provided by the user"""

        return self.deck_list[index_number]


exemplar_card_deck = CardsDeck(Card.number_list, Card.mast_list)
exemplar_card_deck.deck_shuffle()

card_selected_index = int(input("There are 54 cards in the deck. "
                                "Select the sequence number of the card "
                                "you want to reveal... ")) - 1
card_selected_instance = exemplar_card_deck.deck_get(card_selected_index)
print(f"The card you have chosen is a {card_selected_instance.number}"
      f" of {card_selected_instance.mast}!")
