# ---------------------------------------- #
# Author   : Ashok Koduru
# Project  : 2python-random
# Date     : 04th 12, 2017
# Created in PyCharm
# ---------------------------------------- #

import sys, pygame, Buttons
import Dealer, AIAgent, util
import CardDeckandShoe
from AIAgent import *

def main_game(agent):

    return None


if __name__ == "__main__":
    def_epsilon = 0.8
    def_gamma = 0.8
    def_alpha = 0.9
    args = sys.argv
    Agent = None
    if len(args) == 2:
        Agent = FeatureAgent(int(args[1]), util.Counter(), def_epsilon, def_gamma, def_alpha)
    elif len(args) == 3:
        Agent = FeatureAgent(int(args[1]), util.Counter(), def_epsilon, def_gamma, def_alpha, int(args[2]))
    elif len(args) == 4:
        if int(args[3]) == 1:
            Agent = FeatureAgent(int(args[1]), util.Counter(), def_epsilon, def_gamma, def_alpha, int(args[2]))
        elif int(sys.argv[3]) == 2:
            print "QLearning Started"
            Agent = QLearningAgent(int(args[1]), util.Counter(), def_epsilon, def_gamma, def_alpha, int(args[2]))
    else:
        Agent = FeatureAgent(1, util.Counter(), def_epsilon, def_gamma, def_alpha)
    main_game(Agent)
