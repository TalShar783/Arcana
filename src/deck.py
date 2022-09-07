import random
import cards
import hunterCards
# TODO: Add documentation.


class DeckClass:
    def __init__(self, card_set=cards):
        self.myCards = []
        self.originalCards = []
        self.card_set = card_set
        self.build()

    def build(self):
        for p in self.card_set.CardClass.registry:
            self.myCards.append(p)
        for c in self.card_set.CardClass.registry:
            self.originalCards.append(c)
        random.shuffle(self.myCards)

    def getCardSet(self):
        return self.card_set

    def setCardSet(self, in_set):
        self.card_set = in_set
        return

    def drawCard(self):
        if len(self.myCards) <= 1:
            chosenCard = self.card_set.errored_card
            print("You've run out of cards!")
            return chosenCard
        chosenCard = self.myCards[0]
        if chosenCard.n == "Error":
            self.myCards.append(self.myCards.pop(self.myCards.index(self.myCards[0])))
            chosenCard = self.myCards[0]
        try:
            self.myCards.remove(chosenCard)
            return chosenCard
        except IndexError:
            chosenCard = self.card_set.errored_card
            print("You've run out of cards!")
            return chosenCard

    def drawCardWithoutRemove(self):
        if len(self.myCards) <= 1:
            chosenCard = self.card_set.errored_card
            print("You've run out of cards!")
            return chosenCard
        chosenCard = self.myCards[0]
        if chosenCard.n == "Error":
            self.myCards.append(self.myCards.pop(self.myCards.index(0)))
            chosenCard = self.myCards[0]
        try:
            return chosenCard
        except IndexError:
            chosenCard = self.card_set.errored_card
            print("You've run out of cards!")
            return chosenCard

    def pickCard(self, card: str):
        chosenCard = None
        try:
            for c in self.myCards:
                if card.lower() == c.n.lower():
                    chosenCard = c
                    if chosenCard.n != "Error":
                        self.myCards.remove(chosenCard)
                    return chosenCard
            print("Card not found in deck!")
            return self.card_set.errored_card
        except IndexError | AttributeError:
            chosenCard = cards.errored_card
            print("You've run out of cards!")
            return chosenCard

    def shuffle(self):
        self.myCards = []
        self.build()

    def show(self):
        for c in self.myCards:
            print(c.show())

    def cardsRemaining(self):
        return len(self.myCards)

# thisDeck = DeckClass()
# card = thisDeck.drawCard()
# print(card.show())
# for x in range (0,len(thisDeck.cards)):
#     print(thisDeck.drawCard().n)

# for n in thisDeck.cards:
#     print(n.n)
