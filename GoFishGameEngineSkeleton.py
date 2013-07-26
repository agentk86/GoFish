from CardTools import *
import random

#######################################################
#######################################################
################FUNCTION DEFINITIONS###################



#######################################################
#######################################################

##printing some welcome message indicating the begining
##of the program
print("~"*70)
print("~"*25+"WELCOME TO GO FISH!"+"~"*26)
print("~"*70)

##how many players
nPlayers = 4

## index of human player
nHumanPlayer = 0

##how many cards initially on each hand 
nCards = 10

##get a deck of cards, see the SetDeck()
##for details on how each card is represented
deck = SetDeck()

##shuffle the deck of cards
sDeck = Shuffle(deck[:])

##deal nCards to each player and collect
##all the hands in a list of lists,
##see DealInitialCards(nPlayers,nCards,sDeck)
##for details on the list of lists pHands
pHands = DealInitialCards(nPlayers,nCards,sDeck)

##sorting the human player's hand
##for easier reading.
##player 0 is the human player and
##pHands[0] is his/her hand.
##no point in sorting the other player's
##hand as they are computer controlled
##and we need not view those cards ;)
##Sort(pHands[0])

##show the human player his/her cards
##ShowCards(nHumanPalyer,pHands[nHumanPalyer])

## Game playing loop
nTurn = 1
nPicked = 0
pBooks = [[],[],[],[]]

##LogCardsInHands(pHands)
bEnd = EndOfCardGame(sDeck, pHands)
while not bEnd:
    nPicked = DealTurn(nTurn, nPicked, sDeck, pHands)
    DealBooks(pHands, pBooks)
    ShowBooks(pBooks)
    ##LogCardsInHands(pHands)
    nTurn += 1
    bEnd = EndOfCardGame(sDeck, pHands)
    if not bEnd:
        raw_input("Press a key to continue")

ShowGameResult(pBooks)

## show game result

##################################################
##################################################
##                                              ##
##            COMPLETE THE PROGRAM              ##
##                                              ##
