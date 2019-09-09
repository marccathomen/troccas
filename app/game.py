from deck import Card
from deck import Deck
from player import Player


class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = []
        i = 0
        for i in range(1, 5):
            self.players.append(Player(i, "Player " + str(i)))

    def show_players(self):
        for p in self.players:
            p.show()

    def deal_cards(self):
        pass
