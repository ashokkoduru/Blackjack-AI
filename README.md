The following files are Included:

Blackjack.py - Main Game
CardDeckandShoe.py - Card, Deck and Shoe classes
Dealer.py - Blackjack game logic along with player 
AIAgent.py - Feature Extraction Agent and QLearning Agent implemented
FeatureExtractors.py - Features used by FeatureAgent
util.py - Some utility functions

python Blackjack.py

There are 3 arguments, 
1. Number of decks in play,
2. Number of test games
3. Third one is the agent which needs to be trained
    1 is the Feature  Extraciotn Agent, 
    2 is the QLearning Agent.

How to run the code.

python Blackjack.py 3 500 2

the above line indicates 
    1. The game is played with 3 decks
    2. 500 games are being player for training
    3. Q Learning agent is used in this case

The default parameters are 1 deck, 1000 games, and the FeatureExtraction Agent.