from Deck import Deck


def main():
    # testing the Deck and Card objects

    # create deck of cards
    myDeck = Deck()
    # view all cards in deck
    for card in myDeck.cards:
        print(card.toString())

    # shuffle deck
    myDeck.shuffleDesk()
    print()

    # make sure the deck is shuffled
    for card in myDeck.cards:
        print(card.toString())

    # deal two cards
    card1 = myDeck.dealACard()
    card2 = myDeck.dealACard()

    # verify cards dealt
    print()
    print(card1.toString(), ", Value:", card1.getValue())
    print(card2.toString(), ", Value:", card2.getValue())
    print("Current value of hand:", card1.getValue() + card2.getValue())

    # add cards to my hand
    playerHand = []
    playerHand.append(card1)
    playerHand.append(card2)

    print()
    print("Player Hand:")
    # print player hand
    for aCard in playerHand:
        print(aCard.toString())


main()
