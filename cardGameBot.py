import copy
import random

class CardDeck:
    def __init__(self,debug=False):
        self.baseCards = [0,1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8,9]
        self.graveyard = []
        if debug:
            self.cards = copy.deepcopy(self.baseCards)
        else:
            self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.cards = copy.deepcopy(self.baseCards)
        random.shuffle(self.cards)
        self.graveyard = []

class Player:
    def __init__(self,nickName):
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.points = 0
        self.playerList = []
        self.nickName = nickName
        self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.handCard = None
        self.drawnCard = None
        self.inRound = True
        self.isSafe = False
        self.cardList = []
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
    def priest(self,player):
        print("HandCard of ",player.nickName,": ",player.cardList[0])
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
        self.cardList.append(card)
        if self.handCard == None:
            self.handCard = card
        else:
            self.drawnCard = card

    '''See placed card'''
    def place(self):
        if 9 in self.cardList:
            if [x for x in self.c ardList if x != 9][0] >= 3:
                choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
                while choice != 9:
                    choice = int(input("Jk, you can only pick " + str(9) + ": "))
                self.graveyard.append(9)
                self.cardList.remove(9)
                return

        if 7 in self.cardList:
            if [x for x in self.cardList if x != 7][0] in [5,6]:
                choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
                while choice != 7:
                    choice = int(input("Jk, you can only pick " + str(7) + ": "))
                self.graveyard.append(7)
                self.cardList.remove(7)
                return

        choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
        while choice not in self.cardList:
            choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
        if choice == 2:
            vulnerableList = [x.nickName for x in self.playerList if x.nickName != self.nickName and x.isSafe is False and x.inRound is True]
            if len(vulnerableList) == 0:
                vulnerableList = [self.nickName]
            enemy = input("Pick an opponent: "+str(vulnerableList)+": ")
            while enemy not in vulnerableList:
                enemy = input("Pick an actual opponent: "+str(vulnerableList)+": ")
            self.cardActs[choice]([x for x in self.playerList if x.nickName == enemy][0])
            self.graveyard.append(2)
            self.cardList.remove(2)
        if choice == 8:
            self.graveyard.append(8)
            self.cardList.remove(8)
            self.inRound = False
        if choice == 0:
            self.graveyard.append(0)
            self.cardList.remove(0)
        
        pass

class CardBot:
    def __init__(self):
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.points = 0
        self.playerList = []
        self.nickName = "Botty"
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
        self.cardList = []
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
        self.cardList.append(card)
        if self.handCard == None:
            self.handCard = card
        else:
            self.drawnCard = card
        pass

    '''See placed card'''
    def place(self, card):
        self.cardActs[card]()
        if card == self.handCard:
            self.handCard = self.drawnCard
        self.drawnCard = None
        pass