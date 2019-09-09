#!/usr/bin/python
import time


print("Hello World of Troccas")


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
        print("id:{} power:{} value:{} suit:{} label:{}".format(
            self.id, self.power, self.value, self.suit, self.label))


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for c in self.cards:
            c.show()

    def build(self):
        # build number cards of spadas and bastuns
        id = 0
        power = 0
        value = 0
        for suit in ["Spadas", "Bastuns", "Cuppas", "Rosas"]:
            i = 0
            for label in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "C", "D", "K"]:
                i += 1
                id += 1
                if suit == "Spadas" or suit == "Bastuns":
                    power = i
                    value = 0
                else:
                    power = 11 - i
                    value = 0
                if label == "B":
                    power = 11
                    value = 2
                if label == "C":
                    power = 12
                    value = 3
                if label == "D":
                    power = 13
                    value = 4
                if label == "K":
                    power = 14
                    value = 5
                self.cards.append(Card(id, power, value, suit, label))
                #print(id, power, value, suit, label)


class Player:
    def __init__(self):
        pass


deck = Deck()
deck.show()
print("Number of Cards in Deck: ", len(deck.cards))
print("end")
