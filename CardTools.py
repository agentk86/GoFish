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

    print "Player "+str(player)+" has: " + ' '.join(cards)
    
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
    print("****************************************************")
    
    return

def PickRandomCard(cards):
    """
    Pick a card randomly
    
    cards: from which card list we will pick the random card.
    
    """
    
    Shuffle(cards)
    for item in cards:
        return item
    
def PickRandomPlayer(total, exclude):
    
    """
    Pick a player randomly.

    total: How many Players
    exclude:  Which palyer should be excluded from being pciked

    This function return hitman player's ID/index.
    """
    ## Decreased by 1 so start player index is 0 
    hitman = random.randint(1, total) - 1
    
    while(hitman is exclude):
        ## Decreased by 1 so start player index is 0 
        hitman = random.randint(1, total) - 1
        
    ## ShowMessage("Player " + str(hitman) + " has been randomly hitman as targeted")

    return hitman

def EndOfCardGame(deck, hands):
    '''
    Check if the game is over
    
    deck: fishing decks
    hands: player's cards in hand    
    '''
    gameover = (len(deck) == 0 or len(hands[0]) == 0 or len(hands[1]) == 0 or len(hands[2]) == 0 or len(hands[3]) == 0)
    
    if gameover:
        if len(deck) == 0:
            ShowMessage("GAMEOVER: No more cards left in the deck.")
        for i, cards in enumerate(hands):
            if len(cards) == 0:
                ShowMessage("GAMEOVER: Player " + str(i) + " has no more cards left in his/her hand.")
                
    return gameover

def DealTurn(turn, hitman, deck, hands):  
    '''
    Deal a turn
    '''
    ShowMessage("TURN " + str(turn) + ": Player " + str(hitman) + ", its your turn")
    
    ## Show the card if hitman is a human player
    if IsHumanPlayer(hitman):
        Sort(hands[int(hitman)])
        ShowCards(hitman, hands[int(hitman)])
    
    ## Process this turn 
    if IsHumanPlayer(hitman):
        nextTurn = AskCardByHuman(int(hitman), deck, hands)
    else:
        nextTurn = AskCardByComputer(int(hitman), deck, hands)
    
    return nextTurn
    
def AskCardByComputer(hitman, deck, hands):
    '''
    Ask a card as a computer player
    '''
    ## By default hitman player of next turn will still be current hitman
    nextPicked = hitman
    
    ## Randomly pick something
    nAskHand = PickRandomPlayer(len(hands), hitman)
    nAskCard = PickRandomCard(hands[hitman])
    
    ## Deal Target & Fishing
    if not DealTarget(hitman, int(nAskHand), nAskCard[:1], hands):
        if  not DealFishing(hitman, nAskCard[:1], deck, hands):
            nextPicked = nAskHand
            
    return nextPicked

def AskCardByHuman(hitman, deck, hands):
    '''
    Ask a card as a human player
    
    This function return a player ID as next turn's hitman
    '''
    nextPicked = hitman
    nAskHand = None
    while (nAskHand not in ['1', '2', '3']):
        if (nAskHand != None):
            print ("Error: Must type a valid player id (from 1 to 3)")
        nAskHand = raw_input('Who do you want to ask? (1-3)?')
    
    ## List all ranks
    rank = []
    for card in hands[hitman]:
        if (card[:1] not in rank):
            rank.append(card[:1])
        
    ## Get input    
    nAskCard = None
    while (nAskCard not in rank):
        if (nAskCard != None):
            print ("Error: Must type one of the following valid single character card ranks")
            print ",".join(rank)
        nAskCard = raw_input('What rank are you seeking?(' + ','.join(rank) + ')')

    ## Deal Target & Fishing
    if not DealTarget(hitman, int(nAskHand), nAskCard, hands):
        if  not DealFishing(hitman, nAskCard, deck, hands):
            nextPicked = nAskHand

    return nextPicked
        
def DealTarget(hitman, target, askedRank, hands):
    '''
    Dealing with a targeted player & card
    '''    
    success = False
    
    ShowMessage("TARGET: Player " + str(target) + " is being targeted for the rank <" + str(askedRank) + ">")
    
    transfered = []
    for item in hands[target]:
        if (item[:1] == askedRank):
            success = True
            hands[hitman].append(item)
            transfered.append(item)
    
    ## Remove transfered cards from target
    for item in transfered:
        hands[target].remove(item)
        
    if success:
        ## Display success message        
        ShowMessage("HIT: " + str(len(transfered)) + " card(s) transferred")
        
    return success

def DealFishing(hitman, askedRank, deck, hands):
    '''
    Fish a card from the deck
    '''
    ## By default, assumed its not success
    success = False
    
    ## Fished a card from the deck
    fished = GetTopCard(deck)
    hands[hitman].append(fished)
    
    ## If fished card == askedRank
    if (fished[:1] == askedRank):        
        success = True
        
    if success:
        ## Display successed fished message
        ShowMessage("HIT: LUCKILY Player " + str(hitman) + " has fished up a rank <" + str(fished[:1]) + ">")
    else:
        ## Display missed message        
        if IsHumanPlayer(hitman):
            ShowMessage("MISS: You fished up the rank <" + str(fished[:1]) + ">")
        else:
            ShowMessage("MISS")
        
    return success


def IsHumanPlayer(hitman):
    """
    Check if hitman is a human
    """
    return hitman == 0

def DealBooks(hands, books):
    """
    Check players books in hand
    """
    ## GetSetGameResult.books = []
    ##print "DealBooks Start"
    ##print locals()
    for index in range(0, len(hands) -1):
        books[index] += FindBooks(hands[index])
    ##print "DealBooks End"
    ##print locals()
    return

def FindBooks(cards):
    """
    Find books and remove book items from cards
    
    cards: card list array
    
    Return found books
    """
    books = []
    
    for card in cards:
        if (len([elem for elem in cards if elem[:1] == card[:1]]) == 4):
            ## Found a book
            if (card[:1] not in books):
                books.append(card[:1])

    ## Remove cards already booked
    for book in books:
        for matched in ([elem for elem in cards if elem[:1] == book]):
            cards.remove(matched)

    return books

def ShowBooks(books):
    """
    Show books players have
    
    books: a list contains each player's book (as generated by FindBooks(cards))
    
    This function does not return anything
    """
    ShowMessage("BOOKS")
    
    for i, book in enumerate(books):
        print "Player " + str(i) + ":" + "[" + ",".join(book) + "]"
    
    return

def ShowGameResult(books):
    """
    Show game winners
    
    books: books in players hand
    
    This function does not return anything
    """
    ## ShowMessage("Game Result")
    
    mostBook = [0,0,0,0]
    winners = []
    
    for i, book in enumerate(books):
        mostBook[i] = len(book)
        
    if (max(mostBook) > 0):
        for i, most in enumerate(mostBook):
            if (most == max(mostBook)):
                winners.append(i)
    
    if len(winners) > 0:        
        print "*************Winner(s)*************"
        print ",".join(["Player " + str(s) for s in winners])
        print "CONGRATULATIONS!!"
        print "***********************************"
    
    return

def LogCardsInHands(hands):
    """
    Show cards in players hand
    
    hands:  a list contain <nCards> number of strings where
    each string represents a card
    
    The function does not return anything.
    """
    ShowMessage("Logs")
    
    for i, cards in enumerate(hands):
        Sort(cards)
        print "Player " + str(i) + ": " + ",".join(cards)
    
    return