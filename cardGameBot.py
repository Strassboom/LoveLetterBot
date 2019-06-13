import copy
import random

class CardDeck:
    def __init__(self):
        self.baseCards = [0,1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8,9]
        self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.cards = copy.deepcopy(self.baseCards)
        random.shuffle(self.cards)
        self.graveyard = []

class Player:
    def __init__(self):
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.points = 0
        self.playerList = []
        self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.handCard = None
        self.drawnCard = None
        self.inRound = True
        self.isSafe = False
        self.graveyard = []

    '''Opponent is out if current card is a mercenary'''
    def mercenary(self):
        pass
    
    '''Opponent is out if their card is guessed correctly'''
    def guard(self,card):
        if card == 0:
            print("out")
        pass

    '''Get opponent's card'''
    def priest(self):
        pass

    '''Compare hands with opponent, lowest hand is out'''
    def baron(self):
        pass

    '''Protects player from all effects until their next turn'''
    def handmaid(self):
        pass

    '''Opponent discards their hand and redraws'''
    def prince(self):
        pass

    '''Trade hands with opponent'''
    def king(self):
        pass

    '''Discard if held with 5 or 6'''
    def countess(self):
        pass

    '''Lose if discarded'''
    def princess(self):
        pass

    '''Discard if held with 3 or higher'''
    def emperor(self):
        pass

    '''Draw a card'''
    def draw(self, card):
        if self.handCard == None:
            self.handCard = card
        else:
            self.drawnCard = card

    '''See placed card'''
    def place(self, card):
        self.cardActs[card]()
        pass

class CardBot:
    def __init__(self):
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.points = 0
        self.playerList = []
        self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.cardGraph = [
            [0],
            [0,0,0,0,0],
            [0,0],
            [0,0],
            [0,0],
            [0,0],
            [0],
            [0],
            [0],
            [0]
        ]
        self.handCard = None
        self.drawnCard = None
        self.inRound = True
        self.isSafe = False
        self.graveyard = []

    '''Opponent is out if current card is a mercenary'''
    def mercenary(self):
        pass
    
    '''Opponent is out if their card is guessed correctly'''
    def guard(self):
        pass

    '''Get opponent's card'''
    def priest(self):
        pass

    '''Compare hands with opponent, lowest hand is out'''
    def baron(self):
        pass

    '''Protects player from all effects until their next turn'''
    def handmaid(self):
        pass

    '''Opponent discards their hand and redraws'''
    def prince(self):
        pass

    '''Trade hands with opponent'''
    def king(self):
        pass

    '''Discard if held with 5 or 6'''
    def countess(self):
        pass

    '''Lose if discarded'''
    def princess(self):
        pass

    '''Discard if held with 3 or higher'''
    def emperor(self):
        pass

    '''Draw a card'''
    def draw(self, card):
        if self.handCard == None:
            self.handCard = card
        else:
            self.drawnCard = card
        pass

    '''See placed card'''
    def place(self, card):
        self.cardActs[card]()
        pass