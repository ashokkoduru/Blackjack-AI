# ---------------------------------------- #
# Author   : Ashok Koduru, Bhushan Mohite
# Project  : Blackjack-AI
# Date     : 02th 12, 2017
# Created in PyCharm
# ---------------------------------------- #

import random


class Card:

    def __init__(self, rank, suit, id):
        self.rank = rank
        self.suit = suit
        self.id = id


class Deck:

    def __init__(self):
        self.cards = []
        card_id = 0

        for suit_ctr in range(1, 5):
            for rank_ctr in range(1, 14):
                self.cards += [Card(rank_ctr, suit_ctr, card_id)]
                card_id += 1

    def draw_card_from_deck(self):
        return self.cards.pop()

    def is_deck_empty(self):
        return len(self.cards) == 0

    def card_back_to_deck(self, c):
        return self.cards.append(c)

    def shuffle_deck(self):
        random.shuffle(self.cards)


class Shoe:

    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.decks = [Deck() for _ in range(number_of_decks)]

    def shuffle_shoe(self):
        random.shuffle(self.decks)
        for deck in self.decks:
            deck.shuffle_deck()

    def draw_card_from_shoe(self):
        for deck in self.decks:
            if not deck.is_deck_empty():
                return deck.draw_card_from_deck()

