import random


class Dealer:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def deal_6(self):
        pass

    def full_shuffle(self):
        for i in range(len(self.deck.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.deck.cards[i], self.deck.cards[r] = self.deck.cards[r], self.deck.cards[i]

    def draw_one(self):
        pass
