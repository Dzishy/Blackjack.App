class Player ():
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.playingHand = True
    
    def playersHand(self, deck):
        for i in range (2):
            card = deck.drawCard()
            self.hand.append (card)
            
    def displayHand (self):
        print ('\nPlayers Hand:')
        for card in self.hand:
            card.displayCard()        
    
    def hit (self, deck):
        card = deck.drawCard()
        self.hand.append (card)  
        
    def getHandValue (self):
        self.handValue = 0        # we need to set it to 0 again, because every time we deal cards the value in the init method will we not 0, and we need 0.
        aceInHand = False
        
        for card in self.hand:
            self.handValue += card.value
            if card.rank == 'A':
                aceInHand = True
        if self.handValue > 21 and aceInHand:
            self.handValue -= 10  
        
        print (f'Total value: {self.handValue}')    
                        
    def updateHand (self, deck):
        if self.handValue < 21:
            choice = input ('Would you like to hit (y/n): ').lower()
            if choice == 'y':
                self.hit (deck)
            else:
                self.playingHand = False
        else:
            self.playingHand = False
    