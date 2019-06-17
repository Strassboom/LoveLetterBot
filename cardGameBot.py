import copy
import random

class CardDeck:
    def __init__(self,debug=False):
        # self.baseCards = [0,1,1,1,1,1,2,2,3,3,4,4,5,5,6,7,8,9]
        self.baseCards = [0,1,1,1,1,1,5,2,2,3,4,4,5,6,3,7,1,8]
        self.graveyard = []
        self.maxPoints = 5
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
    def __init__(self,nickName,deck):
        self.cardActs = [self.mercenary,self.guard,self.priest,self.baron,self.handmaid,self.prince,self.king,self.countess,self.princess,self.emperor]
        self.points = 0
        self.playerList = []
        self.nickName = nickName
        self.deck = deck
        self.newRound()

    '''Resets attributes for new round'''
    def newRound(self):
        self.inRound = True
        self.isSafe = False
        self.cardList = []
        self.graveyard = []

    '''Opponent is out if current card is a mercenary'''
    def mercenary(self):
        pass
    
    '''Opponent is out if their card is guessed correctly'''
    def guard(self,enemy):
        while True:
            try:
                guess = int(input("Make a guess: "))
                while guess not in range(len(self.cardActs)-1):
                    guess = int(input("Make a guess: "))
                if enemy.cardList[0] == guess:
                    print("target is out")
                    enemy.inRound = False
                    enemy.graveyard.append(enemy.cardList[0])
                    enemy.cardList.remove(enemy.cardList[0])
                if enemy.cardList[0] == 0:
                    print("Guesser is out")
                    self.inRound = False
                    self.graveyard.append(self.cardList[0])
                    self.cardList.remove(self.cardList[0])
                break
            except ValueError:
                print("guess must be an integer")
                continue
        pass

    '''Get opponent's card'''
    def priest(self,player):
        if self.nickName != player.nickName:
            print("HandCard of ",player.nickName,": ",player.cardList[0])
        pass

    '''Compare hands with opponent, lowest hand is out'''
    def baron(self,player):
        if self.cardList[0] > player.cardList[0]:
            player.inRound = False
            print(player.nickName,"is out")
        elif self.cardList[0] < player.cardList[0]:
            self.inRound = False
            print(self.nickName,"is out")
        else:
            print("A tie! Nothing Happens!")
        pass

    '''Protects player from all effects until their next turn'''
    def handmaid(self):
        self.isSafe = True
        pass

    '''Opponent discards their hand and redraws'''
    def prince(self,player):
        card = player.cardList[0]
        player.graveyard.append(card)
        player.cardList.remove(card)
        if card == 8:
            player.inRound = False
        else:
            newCard = self.deck.cards.pop()
            player.cardList.append(newCard)
        pass

    '''Trade hands with opponent'''
    def king(self,player):
        temp = self.cardList[0]
        self.cardList[0] = player.cardList[0]
        player.cardList[0] = temp
        pass

    '''Discard if held with 5 or 6'''
    def countess(self):
        removed = False
        if [x for x in self.cardList if x != 7][0] in [5,6]:
            choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
            while choice != 7:
                choice = int(input("Jk, you can only pick " + str(7) + ": "))
            self.graveyard.append(choice)
            self.cardList.remove(choice)
            print(self.nickName,"Discarded a",choice)
            removed = True
        return removed

    '''Lose if discarded'''
    def princess(self):
        self.inRound = False
        print(self.nickName,"is out")
        pass

    '''Discard if held with 3 or higher'''
    def emperor(self):
        removed = False
        if [x for x in self.cardList if x != 9][0] >= 3:
            while True:
                try:
                    choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
                    while choice != 9:
                        choice = int(input("Jk, you can only pick " + str(9) + ": "))
                    self.graveyard.append(choice)
                    self.cardList.remove(choice)
                    print(self.nickName,"Discarded a",choice)
                    removed = True
                    return removed
                except ValueError:
                    print("guess must be an integer")
                    continue
        return removed

    '''Draw a card'''
    def draw(self, card):
        self.cardList.append(card)

    '''See placed card'''
    def place(self):
        turnEnd = False
        print(self.nickName+"\'s turn: ")

        if self.isSafe:
            self.isSafe = False

        if 9 in self.cardList:
            if self.cardActs[9]():
                turnEnd = True

        elif 7 in self.cardList:
            if self.cardActs[7]():
                turnEnd = True

        while not turnEnd:
            vulnerableList = [player for player in self.playerList if player.isSafe is False and player.inRound is True]
            print("Targetable Players: ",[player.nickName for player in vulnerableList])
            while True:
                try:
                    choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
                    while choice not in self.cardList:
                        choice = int(input("pick one: "+str([x for x in self.cardList])+": "))
                    if choice in [1,2,3,5,6]:
                        if len(vulnerableList) == 1 and vulnerableList[0].nickName == self.nickName:
                            decision = input("Are you sure you want to use this on yourself?: ")
                            if decision == "y":
                                self.graveyard.append(choice)
                                self.cardList.remove(choice)
                                for count,player in enumerate(vulnerableList):
                                    print(count,"->",player)

                            while True:
                                try:
                                    player = int(input("Pick an opponent: "+str(vulnerableList)+": "))
                                    while player not in range(len(vulnerableList)):
                                        player = input("Pick an actual opponent: "+str(vulnerableList)+": ")
                                    self.cardActs[choice](vulnerableList[player])
                                    turnEnd = True
                                    print(self.nickName,"Discarded a",choice)
                                    break
                                except ValueError:
                                    print("Player choice must be an integer")
                                    continue
                        else:
                            self.graveyard.append(choice)
                            self.cardList.remove(choice)
                            vulnerableList = [player for player in self.playerList if self.nickName != player.nickName and player.inRound and not player.isSafe]
                            for count,player in enumerate(vulnerableList):
                                print(count,"->",player.nickName)

                            while True:
                                try:
                                    player = int(input("Pick an opponent: "))
                                    while player not in range(len(vulnerableList)):
                                        player = int(input("Pick an actual opponent: "+str(vulnerableList)+": "))
                                    self.cardActs[choice](vulnerableList[player])
                                    turnEnd = True
                                    print(self.nickName,"Discarded a",choice)
                                    break
                                except ValueError:
                                    print("Player choice must be an integer")
                                    continue

                    if choice in [0,4,7,8,9]:
                        self.graveyard.append(choice)
                        self.cardList.remove(choice)
                        self.cardActs[choice]()
                        turnEnd = True
                        print(self.nickName,"Discarded a",choice)
                    break
                except ValueError:
                    print("choice must be an integer")
                    continue
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
        self.inRound = True
        self.isSafe = False
        self.cardList = []
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