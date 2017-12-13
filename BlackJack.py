# ---------------------------------------- #
# Author   : Ashok Koduru, Bhushan Mohite
# Project  : 2python-random
# Date     : 04th 12, 2017
# Created in PyCharm
# ---------------------------------------- #

import sys, pygame, Buttons
import Dealer, AIAgent, util, os
import CardDeckandShoe
from AIAgent import *


def explore(agent):
    total_score = 0.0
    games_to_play = agent.train_episodes
    while agent.train_episodes > 0:
        agent.dealer.start_game()
        while True:
            prev_state = agent.get_state()
            action_to_take = agent.get_action(prev_state)
            if agent.dealer.player_turn(action_to_take):
                break
            new_state = agent.get_state()
            total_reward = 0
            agent.update(prev_state, action_to_take, new_state, total_reward)
        agent_game_won = agent.dealer.dealer_won
        if agent_game_won:
            total_reward = 1
            total_score += 1
        else:
            total_reward = -1
        agent.update(prev_state, action_to_take, agent.get_state(), total_reward)
        agent.train_episodes -= 1
    print "\n"
    print "Exploring agent won", int(total_score), "out of", games_to_play
    print "Success rate is ", (total_score / games_to_play)
    print "\nTraining Completed\n"
    return agent


def exploit(agent):
    total_score = 0.0
    games_to_play = 0
    agent.set_epsilon(0)
    agent.set_alpha(0.2)
    while games_to_play < 10000:
        agent.dealer.start_game()
        while True:
            prev_state = agent.get_state()
            action_to_take = agent.get_action(prev_state)
            if agent.dealer.player_turn(action_to_take):
                break
            new_state = agent.get_state()
            total_reward = 0
            agent.update(prev_state, action_to_take, new_state, total_reward)
        agent_game_won = agent.dealer.dealer_won
        if agent_game_won:
            total_reward = 1
            total_score += 1
        else:
            total_reward = -1
        Agent.update(prev_state, action_to_take, agent.get_state(), total_reward)
        games_to_play += 1

    print "Exploiting agent won", int(total_score), "out of", games_to_play
    print "Success rate is", (total_score / games_to_play)
    print "\nExploitation Completed\n"
    return agent


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
    explored_agent = explore(Agent)
    exploited_agent = exploit(explored_agent)
