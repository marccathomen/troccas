import random


class Dealer:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players

    def deal_all(self):
        p = []
        for p in self.players:
            for _ in range(0, 19):
                p.hand.append(self.deck.draw_card())

        # last 2 cards go to last player
        p.hand.append(self.deck.draw_card())
        p.hand.append(self.deck.draw_card())

    def full_shuffle(self):
        for i in range(len(self.deck.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.deck.cards[i], self.deck.cards[r] = self.deck.cards[r], self.deck.cards[i]
