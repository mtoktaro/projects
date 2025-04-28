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
            cards.append(i + str(j))
    
    random.shuffle(cards)

    for i in range(player_number):
        for j in range(2):
            players[i].add_card(cards[i * 2 + j])

    for i in players:
        print(i.show_hand())


if __name__ == '__main__':
    main()