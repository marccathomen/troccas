
from game import Game


print("Hello World of Troccas")


game1 = Game()
game1.deck.show()
game1.dealer.full_shuffle()
print("Game 1:")
game1.deck.show()
game1.show_players()
