# ---------------------------------------- #
# Author   : Ashok Koduru, Bhushan Mohite
# Project  : Blackjack-AI
# Date     : 02nd Dec, 2017
# Created in PyCharm
# ---------------------------------------- #

# Code credits:
# http://www-inst.eecs.berkeley.edu/~cs188/sp11/projects/reinforcement/docs/featureExtractors.html

# featureExtractors.py
# --------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html


import sys, os, util


class FeatureExtractor:
    def getFeatures(self, state, action, discarded):
        """
        Returns a dict from features to counts
        Usually, the count will just be 1.0 for
        indicator functions.
        """
        util.raiseNotDefined()


class IdentityExtractor(FeatureExtractor):
    def getFeatures(self, state, action, discarded):
        feats = util.Counter()
        feats[(state, action)] = 1.0
        return feats


class SimpleExtractor(FeatureExtractor):
    def getFeatures(self, state, action, discarded):
        value_player = state[0][0]
        player_contains_ace = state[0][1]
        value_discarded = 0

        features = util.Counter()

        features["bias"] = 1.0

        for each_card in discarded:
            value_discarded += min(10, each_card.rank)

        if action == 1:
            if player_contains_ace:
                features['value_player'] = (31.0 - value_player)/10
            else:
                features['value_player'] = (21.0 - value_player)/10

            discard_feature_value = float(value_discarded)/len(discarded)
            features['discarded'] = 1.0 if discard_feature_value > 9.0 else 0

        elif action == 2:
            if player_contains_ace:
                features['value_player'] = 1.0/(31.0 - value_player)
            elif value_player != 22:
                features['value_player'] = 1.0/(22.0 - value_player)

            discard_feature_value = float(value_discarded)/len(discarded)
            features['discarded'] = 0 if discard_feature_value > 9.0 else 1.0

        features.divideAll(10.0)
        return features
