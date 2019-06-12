import random

class CardDeck:
    def __init__(self):
        self.cards = [0,1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8,9]
        random.shuffle(self.cards)
        self.graveyard = []

class CardBot:
    def __init__(self):
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
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.handCard = None
        self.drawnCard = None


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
    def draw(self):
        pass