import random

from Card import Card

class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = (list(Card.values.keys()))

    def __init__(self):
        self.deck = []

        for suit in self.suits:
            for rank in self.ranks:
                self.deck.append(Card(suit, rank))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()
