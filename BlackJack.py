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
    explored_agent = explore(agent)
    exploted_agent = exploit(explored_agent)
    pygame.init()
    window_size = 900, 740
    green_color = 0, 160, 0
    black_color = 0, 0, 0
    screen = pygame.display.set_mode(window_size)
    screen.fill(green_color)

    card_score = [0]*52

    cards = []
    cards.append("images/cards/Clubs/AC.jpg")
    cards.append("images/cards/Clubs/2C.jpg")
    cards.append("images/cards/Clubs/3C.jpg")
    cards.append("images/cards/Clubs/4C.jpg")
    cards.append("images/cards/Clubs/5C.jpg")
    cards.append("images/cards/Clubs/6C.jpg")
    cards.append("images/cards/Clubs/7C.jpg")
    cards.append("images/cards/Clubs/8C.jpg")
    cards.append("images/cards/Clubs/9C.jpg")
    cards.append("images/cards/Clubs/10C.jpg")
    cards.append("images/cards/Clubs/JC.jpg")
    cards.append("images/cards/Clubs/QC.jpg")
    cards.append("images/cards/Clubs/KC.jpg")
    cards.append("images/cards/Spades/AS.jpg")
    cards.append("images/cards/Spades/2S.jpg")
    cards.append("images/cards/Spades/3S.jpg")
    cards.append("images/cards/Spades/4S.jpg")
    cards.append("images/cards/Spades/5S.jpg")
    cards.append("images/cards/Spades/6S.jpg")
    cards.append("images/cards/Spades/7S.jpg")
    cards.append("images/cards/Spades/8S.jpg")
    cards.append("images/cards/Spades/9S.jpg")
    cards.append("images/cards/Spades/10S.jpg")
    cards.append("images/cards/Spades/JS.jpg")
    cards.append("images/cards/Spades/QS.jpg")
    cards.append("images/cards/Spades/KS.jpg")
    cards.append("images/cards/Hearts/AH.jpg")
    cards.append("images/cards/Hearts/2H.jpg")
    cards.append("images/cards/Hearts/3H.jpg")
    cards.append("images/cards/Hearts/4H.jpg")
    cards.append("images/cards/Hearts/5H.jpg")
    cards.append("images/cards/Hearts/6H.jpg")
    cards.append("images/cards/Hearts/7H.jpg")
    cards.append("images/cards/Hearts/8H.jpg")
    cards.append("images/cards/Hearts/9H.jpg")
    cards.append("images/cards/Hearts/10H.jpg")
    cards.append("images/cards/Hearts/JH.jpg")
    cards.append("images/cards/Hearts/QH.jpg")
    cards.append("images/cards/Hearts/KH.jpg")
    cards.append("images/cards/Diamonds/AD.jpg")
    cards.append("images/cards/Diamonds/2D.jpg")
    cards.append("images/cards/Diamonds/3D.jpg")
    cards.append("images/cards/Diamonds/4D.jpg")
    cards.append("images/cards/Diamonds/5D.jpg")
    cards.append("images/cards/Diamonds/6D.jpg")
    cards.append("images/cards/Diamonds/7D.jpg")
    cards.append("images/cards/Diamonds/8D.jpg")
    cards.append("images/cards/Diamonds/9D.jpg")
    cards.append("images/cards/Diamonds/10D.jpg")
    cards.append("images/cards/Diamonds/JD.jpg")
    cards.append("images/cards/Diamonds/QD.jpg")
    cards.append("images/cards/Diamonds/KD.jpg")

    standbut = Buttons.Button(550, 500, "images/STAND.bmp")
    hitbut = Buttons.Button(550, 375, "images/HIT.bmp")
    againbut = Buttons.Button(550, 375, "images/Again.bmp")
    endbut = Buttons.Button(550, 500, "images/End.bmp")
    pygame.display.set_caption("Blackjack")
    font = pygame.font.SysFont("Arial", 40)
    winMessage = font.render("You Win!", 1, black_color)
    loseMessage = font.render("You Lose!", 1, black_color)
    hitMessage = font.render("Agent Suggests Hit", 1, black_color)
    standMessage = font.render("Agent Suggests Stand", 1, black_color)

    backimg = pygame.image.load("images/cards/Back.jpg")
    backrect = backimg.get_rect()

    while True:
        screen.fill(green_color)
        screen.blit(standbut.image, standbut.rect)
        screen.blit(hitbut.image, hitbut.rect)
        pygame.display.flip()
        Agent.dealer.gameBegin()
        playerHand = Agent.dealer.getPlayerHand()
        dealerHand = Agent.dealer.getDealerHand()
        playerX = 30
        playerY = 300
        dealerX = 450
        dealerY = 0

        oldState = Agent.getState()
        agentAction = Agent.getAction(oldState)

        if agentAction == 1:
            screen.blit(hitMessage, (20, 100))
        else:
            screen.blit(standMessage, (20, 100))

        for card in playerHand:
            id = card.id
            if card_score[id] != 0:
                screen.blit(card_score[id], card_score[id].get_rect().move(playerX, playerY))
            else:
                cardimg = pygame.image.load(cards[id])
                cardrect = cardimg.get_rect()
                screen.blit(cardimg, cardrect.move(playerX, playerY))
                card_score[id] = cardimg
            playerX += 60
            pygame.display.flip()

        id = dealerHand[0].id
        if card_score[id] != 0:
            screen.blit(card_score[id], card_score[id].get_rect().move(dealerX, dealerY))
        else:
            cardimg = pygame.image.load(cards[id])
            cardrect = cardimg.get_rect()
            screen.blit(cardimg, cardrect.move(dealerX, dealerY))
        dealerX += 60
        screen.blit(backimg, backrect.move(dealerX, dealerY))
        pygame.display.flip()

        while True:

            exitLoop = False
            doneFlag = False

            while exitLoop is False:
                k = pygame.event.poll()
                if k.type == pygame.MOUSEBUTTONDOWN:
                    if k.button == 1:
                        if standbut.clicked(k.pos):
                            standbut.press()
                            screen.blit(standbut.image, standbut.rect)
                            pygame.display.flip()
                            doneFlag = Agent.dealer.playerTurn(2)
                            winFlag = Agent.dealer.winFlag
                            exitLoop = True

                        elif hitbut.clicked(k.pos):
                            hitbut.press()
                            screen.blit(hitbut.image, hitbut.rect)
                            pygame.display.flip()
                            doneFlag = Agent.dealer.playerTurn(1)
                            winFlag = Agent.dealer.winFlag
                            exitLoop = True

                if k.type == pygame.MOUSEBUTTONUP:
                    if k.button == 1:
                        standbut.popup()
                        hitbut.popup()
                        screen.blit(hitbut.image, hitbut.rect)
                        screen.blit(standbut.image, standbut.rect)
                        pygame.display.flip()

            screen.fill(green_color)
            oldState = Agent.getState()
            agentAction = Agent.getAction(oldState)
            if agentAction == 1:
                screen.blit(hitMessage, (20, 100))
            else:
                screen.blit(standMessage, (20, 100))

            pygame.display.flip()
            playerHand = Agent.dealer.getPlayerHand()
            dealerHand = Agent.dealer.getDealerHand()
            playerX = 30
            for card in playerHand:
                id = card.id
                if card_score[id] != 0:
                    screen.blit(card_score[id], card_score[id].get_rect().move(playerX, playerY))
                else:
                    cardimg = pygame.image.load(cards[id])
                    cardrect = cardimg.get_rect()
                    screen.blit(cardimg, cardrect.move(playerX, playerY))
                    card_score[id] = cardimg
                playerX += 60
                pygame.display.flip()

            dealerX = 450
            if doneFlag:
                screen.fill(green_color)

                playerX = 30
                for card in playerHand:
                    id = card.id
                    if card_score[id] != 0:
                        screen.blit(card_score[id], card_score[id].get_rect().move(playerX, playerY))
                    else:
                        cardimg = pygame.image.load(cards[id])
                        cardrect = cardimg.get_rect()
                        screen.blit(cardimg, cardrect.move(playerX, playerY))
                        card_score[id] = cardimg
                    playerX += 60

                pygame.display.flip()

                if len(dealerHand) == 1:
                    Agent.dealer.dealerHand.append(Agent.dealer.drawFromShoe())
                for card in dealerHand:
                    id = card.id
                    if card_score[id] != 0:
                        screen.blit(card_score[id], card_score[id].get_rect().move(dealerX, dealerY))
                    else:
                        cardimg = pygame.image.load(cards[id])
                        cardrect = cardimg.get_rect()
                        screen.blit(cardimg, cardrect.move(dealerX, dealerY))
                        card_score[id] = cardimg
                    dealerX += 60
                    screen.blit(againbut.image, againbut.rect)
                    screen.blit(endbut.image, endbut.rect)
                    if winFlag:
                        screen.blit(winMessage, (100, 100))
                    else:
                        screen.blit(loseMessage, (100, 100))
                    pygame.display.flip()

                break
            else:
                id = dealerHand[0].id
                if card_score[id] != 0:
                    screen.blit(card_score[id], card_score[id].get_rect().move(dealerX, dealerY))
                else:
                    cardimg = pygame.image.load(cards[id])
                    cardrect = cardimg.get_rect()
                    screen.blit(cardimg, cardrect.move(dealerX, dealerY))
                dealerX += 60
                screen.blit(backimg, backrect.move(dealerX, dealerY))
                pygame.display.flip()

        exitLoop = False
        while exitLoop is False:
            k = pygame.event.poll()
            if k.type == pygame.MOUSEBUTTONDOWN:
                if k.button == 1:
                    if againbut.clicked(k.pos):
                        againbut.press()
                        screen.blit(againbut.image, againbut.rect)
                        pygame.display.flip()
                        exitLoop = True

                    elif endbut.clicked(k.pos):
                        endbut.press()
                        screen.blit(endbut.image, endbut.rect)
                        pygame.display.flip()
                        sys.exit()

            if k.type == pygame.MOUSEBUTTONUP:
                if k.button == 1:
                    againbut.popup()
                    endbut.popup()
                    screen.blit(againbut.image, againbut.rect)
                    screen.blit(endbut.image, endbut.rect)
                    pygame.display.flip()

    return None

def explore(agent):
    total_score = 0
    games_to_play = agent.train_episodes
    while agent.train_episodes > 0:
        agent.dealer.start_game()
        while True:
            print "play " + str(agent.train_episodes)
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

    print "Exploring agent won", int(total_score), "out of", games_to_play
    print "Success rate is ", (total_score / games_to_play)
    print "\nTraining Completed\n"
    return agent

def exploit(agent):
    total_score = 0
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
    main_game(Agent)
