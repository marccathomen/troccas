class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []

    def show(self):
        print("--------")
        print(self.name)
        print("Number of Cards " + str(len(self.hand)))
        print("--------")
        for h in self.hand:
            h.show()

    def fai_scart(self):  # just remove the first 2 elements for now
        self.hand.pop()
        self.hand.pop()
