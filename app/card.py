class Card:
    def __init__(self, id, power, value, suit, label):
        self.id = id  # unique identification number
        self.power = power  # beating power
        # value of the card in points
        self.value = value
        # suit of the card [r osa,s pada,c uppa,b astun,t rocca,n arr]
        self.suit = suit
        # label as on the real card [1,2,3,...,9,10,b uod, c cavagl, f emna, r etg, n arr, 1,2,...,20,21]
        self.label = label

    def show(self):
        print(self.label, self.suit)
