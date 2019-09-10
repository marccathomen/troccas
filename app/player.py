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
