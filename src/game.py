import cards
import deck
import player
import hunterCards

class GameClass:
    def __init__(self, id, cardSet=cards):
        self.deck = deck.DeckClass(cardSet)
        self.players = []
        self.id = id

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getPlayers(self):
        return self.players

    def addPlayer(self, name):
        newPlayer = True
        for p in self.players:
            if p.name.casefold() == name.casefold():
                newPlayer = False
        if newPlayer:
            addedPlayer = player.Player(name)
            if name not in self.players:
                self.players.append(addedPlayer)
                print("New player added!")
            return addedPlayer
        else:
            return

    def reset(self, card_set=cards):
        self.deck.setCardSet(card_set)
        self.deck.shuffle()
        self.players = []



# thisGame = GameClass(123)
#
# thisGame.trish = thisGame.addPlayer("Trish")
# thisGame.bob = thisGame.addPlayer("Bob")
#
#
# for p in thisGame.players:
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     print(p.name)
#     p.showHand()
#
# thisGame.reset(hunterCards)
#
# thisGame.trish = thisGame.addPlayer("Trish")
# thisGame.bob = thisGame.addPlayer("Bob")
# for p in thisGame.players:
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     p.draw(thisGame.deck)
#     print(p.name)
#     p.showHand()
#
# print(thisGame.deck.cardsRemaining())

# c = 40
# for x in range(c):
#     print(thisGame.trish.draw(thisGame.deck).n)
#     print(thisGame.deck.cardsRemaining())
