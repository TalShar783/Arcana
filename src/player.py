import cards
import deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            print(f"{self.name}: {card.show()}")






thisDeck = deck.DeckClass()

# bob = Player("Bob")
# bob.draw(thisDeck)
# bob.draw(thisDeck)
# bob.draw(thisDeck)
# bob.draw(thisDeck)
# bob.draw(thisDeck)
#
# trish = Player("Trish")
# trish.draw(thisDeck)
# trish.draw(thisDeck)
# trish.draw(thisDeck)
# trish.draw(thisDeck)
# trish.draw(thisDeck)

for x in range(0,45):
    theCard = thisDeck.drawCard()
    try:
        print(theCard.n)
    except AttributeError:
        break

