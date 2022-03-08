import random
import cards
import deck
import player

class GameClass:
    def __init__(self):
        self.deck = deck.DeckClass()
        self.players = []

    def getPlayers(self):
        return self.players

    def addPlayer(self, name):
        newPlayer = True
        for p in self.players:
            if p.name == name:
                newPlayer = False
        if newPlayer:
            addedPlayer = player.Player(name)
            if name not in self.players:
                self.players.append(addedPlayer)
                print("New player added!")
            return addedPlayer
        else:
            return

    def reset(self):
        self.deck.shuffle()
        self.players = []


#
# thisGame = GameClass()
# #
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
#     p.explainHand()
#
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.explainHand()
#
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.explainHand()
# print(thisGame.deck.cardsRemaining())