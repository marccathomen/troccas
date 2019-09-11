import random


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []
        self.points = 0
        self.scart_points = 0  # the points that are in the scart
        self.pile = []  # the cards that this plays won during the game
        self.scart = []  # the cards that the player put aside if he make scart

    def show(self):
        print("--------")
        print(self.name)
        print("Number of Cards " + str(len(self.hand)))
        print("Current Points: " + str(self.points))
        print("--------")
        for h in self.hand:
            h.show()
        print("--- My pile")
        for p in self.pile:
            p.show()
        print("--- My scart")
        for s in self.scart:
            s.show()

    def fai_scart(self):  # just remove the first 2 elements for now
        self.scart.append(self.hand.pop())
        self.scart.append(self.hand.pop())

    def play_card(self):
        return self.hand.pop(random.randrange(len(self.hand)))

    def add_points(self, points):
        self.points + points
