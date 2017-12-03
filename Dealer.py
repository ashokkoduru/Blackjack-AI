# ---------------------------------------- #
# Author   : Ashok Koduru
# Project  : Blackjack-AI
# Date     : 02th 12, 2017
# Created in PyCharm
# ---------------------------------------- #

import CardandDeck

class Dealer:

    def __init__(self, num_of_decks=1, on_hold=False):
        self.num_of_decks = num_of_decks  # Number of decks in play
        self.shoe = CardandDeck.Shoe(num_of_decks)  # Creating a new shoe
        self.hand_player = []  # Cards in the hand of the player
        self.hand_dealer = []  # Cards in the hand of the dealer
        self.value_player = 0  # Value of the player cards
        self.value_dealer = 0  # Value of the dealer cards
        self.player_contains_ace = False
        self.dealer_contains_ace = False
        self.dealer_won = False
        self.on_hold = on_hold
        self.cards_discarded = []
        self.game_done = False
        self.shoe.shuffle_shoe()

    def get_value_player(self):
        return self.value_player

    def get_value_dealer(self):
        return self.value_dealer

    def get_player_contains_ace(self):
        return self.player_contains_ace

    def get_dealer_contains_ace(self):
        return self.dealer_contains_ace

    def get_cards_discarded(self):
        for each_card in self.hand_player:
            self.cards_discarded += [each_card]
        for each_card in self.hand_dealer:
            self.cards_discarded += [each_card]
        return self.cards_discarded

    def get_hand_player(self):
        return self.hand_player

    def get_hand_dealer(self):
        return self.hand_dealer

    def start_game(self):
        self.dealer_won = False
        self.game_done = False
        self.hand_player = []
        self.hand_player = []

        while True:
            self.play()
            self.value_of_hand()
            if self.on_hold:
                return
            else:
                self.player_turn()
            choice = input("\nWant to play another game?\n 1: Y\n 2: N")
            if choice == 2:
                break

    def play(self):
        for i in range(2):
            self.hand_player += [self.get_card_from_shoe()]
        self.hand_dealer += [self.get_card_from_shoe()]

    def get_card_from_shoe(self):
        card = self.shoe.draw_card_from_shoe()
        if card is None:
            self.reshuffle_shoe()
            card = self.shoe.draw_card_from_shoe()
        return card

    def reshuffle_shoe(self):
        self.shoe = CardandDeck.Shoe(self.num_of_decks)
        self.shoe.shuffle_shoe()
        self.cards_discarded = []

    def value_of_hand(self):
        total_value_player = 0
        total_value_dealer = 0
        self.player_contains_ace = False
        self.dealer_contains_ace = False

        for each_card in self.hand_player:
            if each_card.rank == 1:
                self.player_contains_ace = True
            total_value_player += min(10, each_card.rank)

        for each_card in self.hand_dealer:
            if each_card.rank == 1:
                self.dealer_contains_ace = True
            total_value_dealer += min(10, each_card.rank)

        self.value_player = total_value_player
        self.value_dealer = total_value_dealer

    def dealer_turn(self):
        ace_present = False
        self.hand_dealer.append(self.get_card_from_shoe())
        self.value_of_hand()

        if self.value_dealer > 21:
            if not self.on_hold:
                return self.game_over()
            else:
                return self.game_over_on_hold()

        if self.value_dealer > 16:
            if not self.on_hold:
                return self.game_over()
            else:
                return self.game_over_on_hold()

        while self.value_dealer < 17:
            self.hand_dealer.append(self.get_card_from_shoe())
            self.value_of_hand()
            if self.dealer_contains_ace:
                if ace_present:
                    if self.value_dealer == 21:
                        if self.on_hold:
                            return self.game_over_on_hold()
                        else:
                            self.dealer_contains_ace = False
                            return self.game_over()
                    if self.value_dealer > 21:
                        ace_present = False
                        self.value_dealer -= 10
                if self.value_dealer + 10 < 22:
                    ace_present = True
                    self.value_dealer += 10

            if self.value_dealer > 21:
                if self.on_hold:
                    return self.game_over_on_hold()
                else:
                    return self.game_over()

            if self.value_dealer > 16:
                if ace_present:
                    self.value_dealer -= 10
                else:
                    if self.on_hold:
                        return self.game_over_on_hold()
                    else:
                        return self.game_over()

    def player_turn(self, action=2):
        self.value_of_hand()

        if self.value_player > 21:
            if self.on_hold:
                return self.game_over_on_hold()
            else:
                return self.game_over()

        if self.value_player is 21:
            if self.on_hold:
                return self.game_over_on_hold()
            else:
                return self.game_over()

        if self.player_contains_ace:
            if self.on_hold:
                if self.value_player + 10 == 21:
                    return self.game_over_on_hold()
            else:
                if self.value_player + 10 == 21:
                    self.value_player += 10
                    self.player_contains_ace = False
                    return self.game_over()

        while self.value_player < 22:
            if self.on_hold:
                if action == 2:
                    return self.dealer_turn()
                else:
                    self.hand_player.append(self.get_card_from_shoe())
                    self.value_of_hand()
                    if self.value_player > 21:
                        return self.game_over_on_hold()

                    if self.value_player == 21:
                        return self.game_over_on_hold()

                    if self.player_contains_ace:
                        if self.value_player + 10 == 21:
                            return self.game_over_on_hold()
                    return False
            else:
                choice = input("\nPlease Enter\n 1. Hit\n 2. Stand")
                if choice == 2:
                    self.dealer_turn()
                    return

                self.hand_player.append(self.get_card_from_shoe())
                self.value_of_hand()

                if self.value_player > 21:
                    self.game_over()
                    return

                if self.value_player == 21:
                    self.dealer_turn()
                    return

                if self.player_contains_ace:
                    if self.value_player + 10 == 21:
                        self.value_player += 10
                        self.player_contains_ace = False
                        self.dealer_turn()
                        return

    def game_over(self):

        self.hand_player = []
        self.hand_dealer = []

        if self.value_player > 21:
            self.dealer_won = False
        elif self.value_dealer > 21:
            self.dealer_won = True
        elif self.value_player == self.value_dealer:
            self.dealer_won = False
            return True
        elif self.value_player == 21:
            self.dealer_won = True
        elif self.value_dealer == 21:
            self.dealer_won = False
        elif self.value_player > self.value_dealer:
            self.dealer_won = True
        elif self.value_player < self.value_dealer:
            self.dealer_won = False

        return True

    def game_over_on_hold(self):
        for i in range(len(self.hand_player)):
            self.cards_discarded.append(self.hand_player[i])

        for i in range(len(self.hand_dealer)):
            self.cards_discarded.append(self.hand_dealer[i])

        if self.value_player > 21:
            self.dealer_won = False
        elif self.value_dealer > 21:
            self.dealer_won = True
        elif self.value_player == self.value_dealer:
            self.dealer_won = False
            return True
        elif self.value_player == 21:
            self.dealer_won = True
        elif self.value_dealer == 21:
            self.dealer_won = False
        elif self.value_player > self.value_dealer:
            self.dealer_won = True
        elif self.value_player < self.value_dealer:
            self.dealer_won = False

        return True
