class Card:
    value = 0
    suit = ""

    def __init__(self, value, suit):
        self.evalCardValue(value)
        self.evalCardSuit(suit)


    def evalCardValue(self, value):
        self.value = value + 1


    def evalCardSuit(self, suit):
        if suit == 0:
            self.suit = "Spade"
        if suit == 1:
            self.suit = "Heart"
        if suit == 2:
            self.suit = "Club"
        if suit == 3:
            self.suit = "Diamond"

    def toString(self):
        strValue = ""
        if self.value == 1:
            strValue = "Ace"
        elif self.value == 2:
            strValue = "Two"
        elif self.value == 3:
            strValue = "Three"
        elif self.value == 4:
            strValue = "Four"
        elif self.value == 5:
            strValue = "Five"
        elif self.value == 6:
            strValue = "Six"
        elif self.value == 7:
            strValue = "Seven"
        elif self.value == 8:
            strValue = "Eight"
        elif self.value == 9:
            strValue = "Nine"
        elif self.value == 10:
            strValue = "Ten"
        elif self.value == 11:
            strValue = "Jack"
        elif self.value == 12:
            strValue = "Queen"
        elif self.value == 13:
            strValue = "King"

        return strValue + " " + str(self.suit)


    def getValue(self):
        if self.value >= 10:
            return 10
        else:
            return self.value
