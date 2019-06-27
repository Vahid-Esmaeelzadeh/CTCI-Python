import random
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print(self.val, "of", self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Diamonds", "Clubs", "Hearts"]:
            for v in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        random.shuffle(self.cards)

    def drawCard(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, d: Deck):
        self.hand.append(d.drawCard())
        return self

    def showHand(self):
        for c in self.hand:
            c.show()

    def discard(self):
        return self.hand.pop()

card = Card("Hearts", 10)
card.show()

deck1 = Deck()
deck1.show()
deck1.shuffle()
deck1.show()

vahid = Player("Vahid")
vahid.draw(deck1).draw(deck1).draw(deck1).draw(deck1)

print("\nVahid's hand:")
vahid.showHand()
print()
vahid.discard().show()
print()
vahid.showHand()
