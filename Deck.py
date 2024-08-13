import random
from Card import Card

class Deck ():
    def __init__(self):
        self.cards = []        
        
    def buildDeck(self):    
        suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11, }
        
        for suit in suits:
            for key, value in ranks.items():
                card = Card(key, suit ,value)
                self.cards.append(card)
    
    def shuffleCards (self):
        random.shuffle(self.cards)
    
    def drawCard (self):
        return self.cards.pop()