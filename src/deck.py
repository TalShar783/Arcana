import random
import cards


class DeckClass:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for p in cards.CardClass.registry:
            self.cards.append(p)

    def drawCard(self):
        try:
            chosenCard = random.choice(self.cards)
            self.cards.remove(chosenCard)
            return chosenCard
        except IndexError:
            chosenCard = None
            print("You've run out of cards!")
            return
    def shuffle(self):
        self.cards = []
        self.build()
    def show(self):
        for c in self.cards:
            print(c.show())

    def cardsRemaining(self):
        return len(self.cards)




# thisDeck = DeckClass()
# card = thisDeck.drawCard()
# print(card.show())
# for x in range (0,len(thisDeck.cards)):
#     print(thisDeck.drawCard().n)

# for n in thisDeck.cards:
#     print(n.n)