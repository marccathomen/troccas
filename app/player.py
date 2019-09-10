class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.hand = []

    def show(self):
        print("id:{} name:{}".format(
            self.id, self.name))
        for h in self.hand:
            h.show()
