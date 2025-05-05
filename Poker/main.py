import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)
    
    def show_hand(self):
        return self.name, self.hand
        

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
            cards.append((i, str(j)))
    
    total_cards = len(cards)
    random.shuffle(cards)
    
    print(cards[total_cards-10 : total_cards])

    for i in range(player_number):
        for j in range(2):
            players[i].add_card(cards[total_cards - 1])
            cards.pop()
            total_cards -= 1

    for i in players:
        print('Players cards: ', i.show_hand())

    opened_cards = []
    for i in range(5):
        opened_cards.append(cards[total_cards - 1])
        total_cards -= 1
    

    print(opened_cards)

    # assing the best coombinatio to each player
    for player in players:
        check(player, opened_cards)

    
    # choose a player with the highest combination and display the combination
    for i in players: 


    print('Game Over')
if __name__ == '__main__':
    main()