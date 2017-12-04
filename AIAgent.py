# ---------------------------------------- #
# Author   : Ashok Koduru
# Project  : 2python-random
# Date     : 04th 12, 2017
# Created in PyCharm
# ---------------------------------------- #

# Appropriate Code snippets taken from QLearning Assignment of Pacman

import Dealer, util, random, sys

class FeatureAgent:

    def __init__(self, num_of_decks=1, q_values=util.Counter(), epsilon=0.05, gamma=0.8, alpha=0.2, train_episodes=1000, extractor='SimpleExtractor'):
        self.dealer = Dealer.Dealer(num_of_decks, True)
        self.q_values = q_values
        self.epsilon = epsilon
        self.discount = gamma
        self.alpha = alpha
        self.train_episodes = train_episodes
        self.weights = util.Counter()
        self.featExtractor = util.lookup(extractor, globals())()

    def get_legal_actions(self):
        return [1, 2]

    def get_epsilon(self):
        return self.epsilon

    def set_epsilon(self, epsilon):
        self.epsilon = epsilon

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha

    def get_action(self, state):
        legal_actions = self.get_legal_actions()
        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)
        return self.get_policy(state)

    def get_policy(self, state):
        max_value = -99999999
        max_action = None
        legal_actions = self.get_legal_actions()

        for each_action in legal_actions:
            acion_value = self.get_q_value(state, each_action)
            if max_value < acion_value:
                max_value = acion_value
                max_action = each_action

        return max_action

    def get_q_value(self, state, action):
        q_value = 0
        features = self.featExtractor.getFeatures(state, action, self.dealer.get_cards_discarded())
        for action in features.sortedKeys():
            feature = features[action]
            weight = self.weights[action]
            q_value += feature * weight
        return q_value

    def get_state(self):
        return (self.dealer.get_value_player(), self.dealer.get_player_contains_ace()), (self.dealer.get_hand_dealer(), self.dealer.get_dealer_contains_ace())

    def update(self, state, action, next_state, reward):
        features = self.featExtractor.getFeatures(state, action, self.dealer.get_cards_discarded())

        for action in features.sortedKeys():
            weight = self.weights[action] + self.alpha * ((reward + self.discount * self.get_value(next_state)) - self.get_q_value(state, action)) * features[action]
            self.weights[action] = weight

    def get_value(self, state):
        max_value = -99999999
        legal_actions = self.get_legal_actions()
        for each_action in legal_actions:
            action_value = self.get_q_value(state, each_action)
            if max_value < action_value:
                max_value = action_value
        return max_value
