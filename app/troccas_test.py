class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print("{} of {}".format(self.value, self.suit))
        print("caca")


class Deck:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass


card = Card("Card", 2)
card.show()
print("cucu")
