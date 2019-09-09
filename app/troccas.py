from deck import Card
from deck import Deck
from player import Player


print("Hello World of Troccas")


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


game1 = Game()
# game1.deck.show()
game1.deck.full_shuffle()
print("Game 1:")
game1.show_players()
# game1.players.show()
