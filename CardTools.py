import random
import sys
from collections import defaultdict

def SetDeck():
    """
    Setup a new deck of cards.

    The function returns a list of strings where each string
    is a 2 character string representing a card. The first character
    represents the rank of a card and the second character represents
    the suit of a card. For example, "ac" stands for Ace of Clubs

    a = ace, k = king, q = queen, j = jack, t = 10, 9 = 9 and so on
    s = spade, c = club, d = diamond, h = heart
    """
    ##strings representing the suites Clubs,Diamonds,Spades,Hearts
    suitList = ["s", "c", "d", "h"]
    ##strings representing the ranks 2-9,Ten,Jack,Queen,King,Ace
    rankList = ["a", "2", "3", "4", "5", "6", "7", "8", "9", "t", "j", "q", "k"]

    ##we will keep the unshuffled deck of cards here
    deck = []

    ##we create a deck of cards where each card
    ##has a 2 string representation
    ##first string denotes rank, second suit
    for suite in range(4):
        for rank in range(13):
            deck.append(rankList[rank]+suitList[suite])

    return deck

def Shuffle(deck):
    """
    Shuffles a deck of cards.

    deck:   has to be a list, as returned by the
            function SetDeck()

    This function re-orders the elements inside
    the argument <deck> and returns the re-ordered
    <deck>
    """
    nCards = len(deck)

    for i in range(nCards):
        ##select a random integer between
        ##0 and 51
        j = random.randint(i,nCards-1)
        ##swap card[i] with random card
        deck[i], deck[j] = deck[j], deck[i]

    return deck

def GetTopCard(shuffledDeck):
    """
    Gets the top card from a stack of undealt cards.
    
    shuffledDeck:   has to be a list, as returned by the
                    function Shuffle(deck)

    This function returns a 2 character string where the
    string represents a card (as described in SetDeck()).
    This card happens to be the top most card of the
    stack of cards <shuffledDeck>.
    """
    return shuffledDeck.pop(0)

def DealInitialCards(nPlayers,nCards,shuffledDeck):
    """
    Gives all players their initial cards.

    nPlayers:       has to be an integer
    nCards:         has to be an integer
    shuffledDeck:   has to be a list, as returned by the
                    function Shuffle(deck)

    This function returns a list of lists as follows.
    The outer list contains <nPlayers> number of inner lists.
    Each inner list will contain <nCards> number of strings where
    each string represents a card (as described in SetDeck()).
    The cards will be taken from <shuffledDeck> from the top,
    and each player will be assigned a card in turn.
    """
    ##this list of list will have all players cards
    ##each element in the outer list represent a player
    ##the 2 strings in each inner list represent a player's
    ##5 initial cards
    playersCards = [["" for j in range(nCards)] for i in range(nPlayers)]

    ##give each player their first 5 cards, one at a time
    for j in range(nCards):
        for i in range(nPlayers):
            playersCards[i][j] = GetTopCard(shuffledDeck)

    return playersCards

def Sort(cards):
    """
    Sorts the list of cards in place in ascending order.
    Applies bubble sort.

    cards:  has to be a list of strings where each string
            represents a card (as described in SetDeck())

    This function does not need to return anything as it
    sorts the list in place.
    """
    ##the following string has all the ranks in a deck.
    ##notice that the index of each rank tells us its
    ##position in the pecking order, i.e. - the higher
    ##the index the larger the card is. we will use
    ##this index to sort the cards. we are assuming
    ##ace to have the smallest value (0) and king to
    ##have the highest (12)
    rankString = "a23456789tjqk"

    swapped=True
    while swapped:
        ##first we assume there will be no swap
        swapped = False
        ##now time to verify assumption
        for i in range(len(cards)-1):
            if rankString.find(cards[i][0])>rankString.find(cards[i+1][0]):
                ##means two neighbours are in the wrong order
                ##therefore we have to swap the 2 cards
                cards[i],cards[i+1]=cards[i+1],cards[i]
                ##we set swapped to True as we need to pass
                ##through the list again
                swapped = True

    return

def ShowCards(player,cards):
    """
    Displays a player's cards.

    player: could be an integer/string indicating a player
    cards:  has to be a list of strings where each string
            represents a card (as described in SetDeck())

    The function does not return anything.
    """
    print("\n****************************************************")
    print("************Player "+str(player)+" has**************")
    print("****************************************************\n")

    print ' '.join(cards)
    
    return

def ShowMessage(msg):
    """
    Displays a message on the console/shell.

    msg:    could be any message that is to be output
            to the console/shell.

    The function does not return anything.
    """

    print("****************************************************")
    print(str(msg))
    print("****************************************************\n")
    
    return

def PickRandomCard(cards):
    '''
    Pick a card randomly from given cards
    '''
    Shuffle(cards)
    for item in cards:
        return item
    
def PickRandomPlayer(total, exclude = None):
    
    """
    Pick a player randomly.

    total: How many Players
    exclude:  Which should be excluded from being pciked

    This function return picked player's index.
    """

    picked = random.randint(1, total)
    while(picked is exclude):
        picked = random.randint(1, total)
        
    picked = picked -1
    
    return picked

def EndOfCardGame(deck, hands):
    '''
    
    '''
    return len(deck) == 0 or len(hands[0]) == 0 or len(hands[1]) == 0 or len(hands[2]) == 0 or len(hands[3]) == 0

def DealTurn(turn, picked, deck, hands):  
    '''
    
    '''
    ShowMessage("TURN " + str(turn) + ": Player " + str(picked) + ", its your turn")
    Sort(hands[picked])
    ShowCards(picked, hands[picked])
    
    if IsHumanPlayer(picked):
        nextTurn = AskCardByHuman(picked, deck, hands)
    else:
        nextTurn = AskCardByComputer(picked, deck, hands)
    
    return nextTurn
    
def AskCardByComputer(picked, deck, hands):
    '''
    Ask a card as a computer player
    '''
    
    nextPicked = picked
    nAskHand = PickRandomPlayer(len(hands), picked)
    nAskCard = PickRandomCard(hands[picked])
    
    if not DealAskedCard(picked, nAskHand, nAskCard, hands):
        if  not DealFishCard(picked, nAskCard, deck, hands):
            nextPicked = nAskHand
            
    return nextPicked

def AskCardByHuman(picked, deck, hands):
    '''
    Ask a card as a human player
    '''
    nextPicked = picked
    nAskHand = None
    while (nAskHand not in ['1', '2', '3']):
        if (nAskHand != None):
            print ("Invalid input. Please try again.")
        nAskHand = raw_input('Who do you want to ask? (1-3)?')
    
    nAskCard = None
    while (nAskCard not in hands[picked]):
        if (nAskCard != None):
            print ("Invalid input. Please try again")
        nAskCard = raw_input('What rank are you seeking?(' + ' '.join(hands[picked]) + ')')
    
    if not DealAskedCard(picked, nAskHand, nAskCard, hands):
        if  not DealFishCard(picked, nAskCard, deck, hands):
            nextPicked = nAskHand

    return nextPicked
        
def DealAskedCard(picked, askedHand, askedCard, hands):
    '''
    Dealing with asked a card
    '''
    success = False
    
    ShowMessage("TARGET: Player " + str(picked) + " is being targeted for the rank <" + str(askedCard[:1]) + ">")
    
    for item in hands[askedHand]:
        if (item[:1] == askedCard[:1]):
            success = True
            hands[picked].append(item)
            hands[askedHand].remote(item)
    
    if success:
        ## TODO:Display success message        
        ShowMessage("Test")
    else:
        ## TODO:Display missed message
        ShowMessage("Test")
        
    return success

def DealFishCard(picked, askedCard, deck, hands):
    '''
    Fish a card from the deck
    '''
    success = False
    fished = deck.pop()
    hands[picked].append(fished)
    if (fished[:1] == askedCard[:1]):        
        success = True
        
    if success:
        ## TODO:Display successed message
        ShowMessage("Test")
    else:
        ## TODO:Display missed message        
        ShowMessage("Test")
        
    return success


def IsHumanPlayer(picked):
    '''
    Check if given player is a human
    '''
    return picked == 0

def ShowGameResult(hands):
    '''
    Compute game result and display it
    '''
    
    ShowMessage("Game Result")
    
    return