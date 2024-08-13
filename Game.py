

class Game ():
    def __init__(self, money):
        self.money = int (money)
        self.bet = 20   # min bet per hand is $20
        self.winner = ""
    
    def setBet (self):
        betting = True
        while betting:
            bet = int (input ('What would you like to bet (minimum bet of $20): '))
            if bet < 20:
                print ("Your bet is too low. We raised your bet up to $20.")
                bet = 20
                
            if bet > self.money:
                print ('Sorry, you cannot afford that bet.')
            else:
                self.bet = bet
                betting = False
                
    def scoring (self, pVal, dVal):
        
        if pVal == 21:
            print ('You got BLACK JACK! You win!')
            self.winner = 'p'
        elif dVal == 21:
            print ('The dealer got BLACK JACK! You loose!')
            self.winner = 'd'
        
        elif pVal > 21:
            print ('You went over 21... You loose!')
            self.winner = 'd'
        elif dVal > 21:
            print ('Dealer went over 21... You win!')
            self.winner = 'p'
            
        else:
            if pVal > dVal:
                print (f'Dealer gets {dVal}. You win')
                self.winner = 'p'
            elif dVal > pVal:
                print (f'Dealer gets {dVal}. You loose')
                self.winner = 'd'
            else:
                print (f'Dealer gets {dVal}. It is a push...')
                self.winner = 'tie'
                
    def payout (self):
        if self.winner == 'p':
            self.money += self.bet
        elif self.winner == 'd':
            self.money -= self.bet
            
    def displayMoney (self):
        print (f'\nCurrent money: ${self.money}')
        
    def dispMoneyAndBet (self):
        print (f'\nCurrent money: ${self.money}\t\tCurrent bet: ${self.bet}.')
