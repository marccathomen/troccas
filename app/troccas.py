print("Hello World of Troccas")


class Card:
    def __init__(self, id, power, suit, label):
        self.id = id  # unique identification number
        self.power = power  # beating power
        # suit of the card [r osa,s pada,c uppa,b astun,t rocca,n arr]
        self.suit = suit
        # label as on the real card [1,2,3,...,9,10,b uod, c cavagl, f emna, r etg, n arr, 1,2,...,20,21]
        self.label = label

    def show(self):
        # print("id:{} power:{} suit:{} label:{}".format(
         #   self.id, self.power, self.suit, self.label))
        print("caca")


class Deck:
    def __init__(self):
        pass


class Player:
    def __init__(self):
        pass


card = Card(10, 2, "r", "9")
card.show
print("cucu")
