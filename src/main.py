from Deck import Deck
from Player import Player

if __name__ == '__main__':
    new_deck = Deck()
    winner = False

    player_one = Player("One")
    player_one.add_card(new_deck.deck[0:(len(new_deck.deck)//2)])
    print(player_one)

    player_two = Player("Two")
    player_two.add_card(new_deck.deck[(len(new_deck.deck)//2): len(new_deck.deck)])
    print(player_two)

    while not winner:
        if player_one.number_of_cards() == 0:
            print("Player 1 wins!")
            winner = True
        elif player_two.number_of_cards() == 0:
            print("Player 2 wins!")
            winner = True
        else:
            card_one = player_one.remove_one()
            card_two = player_one.remove_one()
            print(f"The card for player 1 is {card_one}")
            print(f"The card for player 2 is {card_two}")
            if card_one.value > card_two.value:
                print(f'The player 1 wins this round, the player 1 has {player_one.number_of_cards()} cards')
                player_one.add_card([card_one, card_two])
            elif card_two.value > card_one.value:
                print(f'The player 2 wins this round, the player 2 has {player_two.number_of_cards()} cards')
                player_two.add_card([card_one, card_two])
            else:
                print('This round is a tie')
                player_one.add_card(card_one)
                player_two.add_card(card_two)


