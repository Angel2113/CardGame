
class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_card(self, cards):
        if type(cards) == type([]):
            self.all_cards.extend(cards)
        else:
            self.all_cards.append(cards)

    def number_of_cards(self):
        return len(self.all_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'