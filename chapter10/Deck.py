import random as random
from Card import Card

class Deck:

    pointer = 0
    cards = []

    def __init__(self):
        #cards = []
        for i in range(4):
            for j in range(13):
                myCard = Card(j, i)
                self.cards.append(myCard)

    def shuffleDesk(self):
        random.shuffle(self.cards)

    def dealACard(self):
        tempCard = self.cards[self.pointer]
        self.pointer += 1
        return tempCard
