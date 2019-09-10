
from game import Game

print("Hello World of Troccas")

game1 = Game()
game1.deck.show()
game1.dealer.full_shuffle()
print("Game 1:")
game1.deck.show()
game1.deck.show_number_cards()
print("Players before dealing:")
game1.show_players()
game1.deal_cards()
print("Players after dealing:")
game1.show_players()
game1.deck.show_number_cards()
