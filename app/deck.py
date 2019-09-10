from card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()

    def show(self):
        for c in self.cards:
            c.show()

    def show_number_cards(self):
        print("Number of Cars in Deck: " + str(len(self.cards)))

    def draw_card(self,):
        return self.cards.pop()

    def build(self):
        id = 0
        power = 0
        value = 0
        suit = ""
        label = ""

        # build number cards of spadas and bastuns
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
                # print(id, power, value, suit, label)
        # build troccas
        suit = "Troccas"
        value = 0
        self.cards.append(Card(57, 15, 5, "Troccas", "1"))  # T1
        id += 1
        for j in range(2, 21):
            id += 1
            power = j + 14
            label = j
            self.cards.append(Card(id, power, value, suit, label))
        self.cards.append(Card(77, 35, 5, "Troccas", "21"))  # T21
        self.cards.append(Card(78, 0, 5, "Narr", "0"))  # N
