from player import Player
from checkcombos import CheckCombos
from output import Output
import random

def main():
    player_number = int(input("Enter number of players:"))

    players = []
    print(player_number)
    for i in range(player_number):
        players.append(Player(f"Player {i}"))

    suits = ['spades', 'hearts', 'diamonds', 'clubs']
    cards = []

    for i in suits:
        for j in range(2, 15):
            cards.append((i, j))
    
    total_cards = len(cards)
    random.shuffle(cards)
    
    for i in range(player_number):
        high_card = 0
        for j in range(2):
            players[i].add_card(cards[total_cards - 1])
            high_card = max(high_card, cards[total_cards - 1][1])
            cards.pop()
            total_cards -= 1
        players[i].highest_card = float(high_card)

    opened_cards = []
    for i in range(5):
        opened_cards.append(cards[total_cards - 1])
        total_cards -= 1
    
    print('Cards on table: ', opened_cards)
    
    for player in players:
        d_numbers = CheckCombos().number_group(player, opened_cards)
        d_suits = CheckCombos().suit_group(player, opened_cards)
        player.best_combo = CheckCombos().all_combos(d_numbers, d_suits)
   
    players = sorted(players, key=lambda x: (x.best_combo, -x.highest_card))
    
    Output().print(players)
if __name__ == '__main__':
    main()