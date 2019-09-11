import random


class Dealer:
    def __init__(self, deck, players):
        self.deck = deck
        self.full_shuffle()
        self.players = players
        self.current_hand = []
        # the player that starts the next hand (default Player 1)
        self.hand_starting_player_id = 1
        # the player that starts the next round of 19 hands (default Player 1)
        self.round_starting_player_id = 1
        # the player that starts the next game of 4 rounds (default Player 1)
        self.game_starting_player_id = 1
        self.hand_points = 0  # points of the hand that was played

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

    def play_hand(self):  # command each player to play one card
        pass
