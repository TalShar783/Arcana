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
        newPlayer = player.Player(name)
        self.players.append(newPlayer)
        return newPlayer

    def reset(self):
        self.deck.shuffle()
        self.players = []



# thisGame = GameClass()
#
# thisGame.trish = thisGame.addPlayer("Trish")
# thisGame.bob = thisGame.addPlayer("Bob")
#
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.draw(thisGame.deck)
# thisGame.trish.showHand()
# thisGame.trish.explainHand()
#
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.draw(thisGame.deck)
# thisGame.bob.showHand()
#
# print(thisGame.deck.cardsRemaining())