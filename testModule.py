import cardGameBot


def fillDeckTest():
    deck = cardGameBot.CardDeck(True)
    cardbot = cardGameBot.CardBot()
    for elem in range(4):
        newCard = deck.cards.pop()
        cardList = cardbot.cardGraph[newCard]
        trueList = [x for x in cardList if x == 1]
        cardList[len(trueList)] = 1
        print(newCard)

    for item in cardbot.cardGraph:
        print(item)

def drawWork():
    deck = cardGameBot.CardDeck(True)
    player1 = cardGameBot.Player("Player1",deck)
    player2 = cardGameBot.Player("Player2",deck)
    cardbot = cardGameBot.Player("thesehoes",deck)
    turns = [player1,player2,cardbot]
    for item in turns:
        item.playerList = turns
        card = deck.cards.pop()
        item.draw(card)
    for item in turns:
        print(item.cardList)

    winners = [player for player in turns if player.points >= deck.maxPoints]
    while len(winners) == 0:
        inList = [player for player in turns if player.inRound]
        while len(inList) > 1:
            for counter,turn in enumerate(turns):
                if turn.inRound == 1:
                    turnCard = deck.cards.pop()
                    turn.draw(turnCard)
                    turn.place()
            inList = [player for player in turns if player.inRound]
        if len(inList) == 1:
            print(inList[0].nickName,"wins the round!")
            inList[0].points += 1
        if inList[0].points == deck.maxPoints:
            print(inList[0].nickName,"wins the game!!!")
        else:
            deck.newRound()
            for player in turns:
                player.newRound()
                card = deck.cards.pop()
                player.draw(card)
        winners = [player for player in turns if player.points >= deck.maxPoints]
drawWork()