import random
import cards


class DeckClass:
    def __init__(self):
        self.cards = []
        self.originalCards = []
        self.build()

    def build(self):
        for p in cards.CardClass.registry:
            self.cards.append(p)
        for c in cards.CardClass.registry:
            self.originalCards.append(c)

    def drawCard(self):
        try:
            chosenCard = random.choice(self.cards)
            while chosenCard.n == "Error":
                chosenCard = random.choice(self.cards)
            self.cards.remove(chosenCard)
            return chosenCard
        except IndexError:
            chosenCard = cards.errored_card
            print("You've run out of cards!")
            return chosenCard

    def pickCard(self, card: str):
        chosenCard = None
        try:
            for c in self.cards:
                if card.casefold() == c.n.casefold():
                    chosenCard = c
                    if chosenCard.n != "Error": self.cards.remove(chosenCard)
                    return chosenCard
            print("Card not found in deck!")
            return cards.errored_card
        except IndexError | AttributeError:
            chosenCard = cards.errored_card
            print("You've run out of cards!")
            return chosenCard


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