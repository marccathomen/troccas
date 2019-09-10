
from game import Game

print("----------------------")
print("Hello World of Troccas")
print("----------------------")

game1 = Game()
print("Deck :")
game1.deck.show()
game1.deck.show_number_cards()
game1.deal_cards()
print("Players after dealing:")
game1.show_players()
game1.deck.show_number_cards()
game1.players[3].fai_scart()
game1.show_players()
print("Players after fa scart:")
game1.deck.show_number_cards()
