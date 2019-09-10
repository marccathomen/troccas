class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []
        self.points = 0

    def show(self):
        print("--------")
        print(self.name)
        print("Number of Cards " + str(len(self.hand)))
        print("Current Points: " + str(self.points))
        print("--------")
        for h in self.hand:
            h.show()

    def fai_scart(self):  # just remove the first 2 elements for now
        self.hand.pop()
        self.hand.pop()

    def add_points(self, points):
        self.points + points
