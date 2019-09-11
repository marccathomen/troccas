class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []
        self.points = 0
        self.pile = []  # the cards that this plays won during the game

    def show(self):
        print("--------")
        print(self.name)
        print("Number of Cards " + str(len(self.hand)))
        print("Current Points: " + str(self.points))
        print("--------")
        for h in self.hand:
            h.show()
        print("My pile")
        
        for p in self.pile:
            p.show()

    def fai_scart(self):  # just remove the first 2 elements for now
        self.pile.append(self.hand.pop())
        self.pile.append(self.hand.pop())

    def add_points(self, points):
        self.points + points

    def play_card(self, table):
        return self.hand.pop()  # just play the first card in the hand
