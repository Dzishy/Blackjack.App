class Card ():
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
        
    def displayCard (self):
        print (f'{self.rank} of {self.suit}')