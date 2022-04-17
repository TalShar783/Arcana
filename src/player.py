import cards
import hunterCards
# TODO: Add documentation.


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        drawnCard = deck.drawCard()
        self.hand.append(drawnCard)
        return drawnCard

    def pick(self, deck, card):
        try:
            pickedCard = deck.pickCard(card)
            self.hand.append(pickedCard)
            return pickedCard
        except IndexError | AttributeError:
            print("No card found!")
            return cards.errored_card

    def showHand(self):
        for card in self.hand:
            print(f"{self.name}: {card.show()}")

    def explainHand(self):
        for card in self.hand:
            print(f"{card.show()}: {card.explain()}")

    def getHand(self):
        myHand = []
        for card in self.hand:
            card.append(myHand)
            return myHand

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName
        return newName






# thisDeck = deck.DeckClass()



#
# # bob = Player("Bob")
# # bob.draw(thisDeck)
# # bob.draw(thisDeck)
# # bob.draw(thisDeck)
# # bob.draw(thisDeck)
# # bob.draw(thisDeck)
# #
# # trish = Player("Trish")
# # trish.draw(thisDeck)
# # trish.draw(thisDeck)
# # trish.draw(thisDeck)
# # trish.draw(thisDeck)
# # trish.draw(thisDeck)
#
# for x in range(0,45):
#     theCard = thisDeck.drawCard()
#     try:
#         print(theCard.n)
#     except AttributeError:
#         break

