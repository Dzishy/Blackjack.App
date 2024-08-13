
class Dealer ():
    def __init__(self):
        self.hand = []
        self.handValue = 0
        self.playingHand = True
    
    def dealersHand(self, deck):
        for i in range (2):
            card = deck.drawCard()
            self.hand.append (card)
            
    def displayHand (self):
        input ("Press 'Enter' to reveal the dealer's hand")
        print (f"\nDealer's hand: ")  
        for card in self.hand:
            card.displayCard() 
             
    
    def hit (self, deck):
        card = deck.drawCard()
        self.hand.append (card) 
        
        while self.handValue < 17:
            card = deck.drawCard()
            self.hand.append (card)
            self.getHandValue()
            
        print (f'\nDealer is set with a total of {len(self.hand)} cards.')
        
    def getHandValue (self):
        self.handValue = 0        # we need to set it to 0 again, because every time we deal cards the value in the init method will we not 0, and we need 0.
        aceInHand = False
        
        for card in self.hand:
            self.handValue += card.value
            if card.rank == 'A':
                aceInHand = True
        if self.handValue > 21 and aceInHand:
            self.handValue -= 10      
 