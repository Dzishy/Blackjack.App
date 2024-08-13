
from Deck import Deck
from Player import Player
from Dealer import Dealer
from Game import Game        

def main ():
    
    print ('Welcome to the Blackjack App.')
    print ('The minimum bet at this table is $20.')

    money = int (input ('\nHow much money are you willing to play with today: '.strip()))
    game = Game(money)

    playing = True
    while playing:
        deck = Deck()
        deck.buildDeck()
        deck.shuffleCards()

        dealer = Dealer()
        player = Player()
        
        game.displayMoney()
        game.setBet()
        game.dispMoneyAndBet()
        
        player.playersHand(deck)
        dealer.dealersHand(deck)
        
        print (f"The dealer is showing {dealer.hand[0].rank} of {dealer.hand[0].suit}")
        
        while player.playingHand:
        
            player.displayHand()
            player.getHandValue()
            player.updateHand(deck)
    
        dealer.hit(deck)
        dealer.displayHand()
        
        game.scoring(player.handValue, dealer.handValue)
        game.payout()
        
        choice = input ('Would you like to bet again (y/n): ')
        if choice != 'y':
            playing = False
            print(f"Your payout: ${game.money}")
        
        if game.money < 20:
            playing = False
            print("Sorry, you ran out of money.  Please try again.")


main()