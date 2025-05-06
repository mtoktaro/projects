import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.best_combo = 100
        self.highest_card = 0
    
    def add_card(self, card):
        self.hand.append(card)
    
    def show_hand(self):
        return self.name, self.hand
        

class CheckCombos:
    def suit_group (self, player, opened_cards):
        d = {}
        for card in player.hand + opened_cards:   
            d[card[0]] = d.get(card[0], [])
            d[card[0]].append(card[1])
        
        return d
    def number_group(self, player, opened_cards):
        d = {}
        for card in player.hand + opened_cards:   
            d[card[1]] = d.get(card[1], [])
            d[card[1]].append(card[0])
        
        return d
        
    def flush(self, players, opened_cards):

        for player in players:
            d = CheckCombos().suit_group(player, opened_cards)
            
            for suit, cards in d.items():
                if len(cards) == 5:
                    print(player.name, 'total cards: ', d)
                    return player.name
        
        return False


    def all_combos(self, d):
        if CheckCombos().four_of_kind(d):
            return 1
        elif CheckCombos().three_of_kind(d) and CheckCombos().pair(d):
            return 2
        elif CheckCombos().three_of_kind(d):
            return 3
        elif CheckCombos().pair(d):
            return 4
    
    def four_of_kind(self, d):
        for cards, suit in d.items():
            if len(suit) == 4:
                return True
        
        return False
    
    def full_house(self, players, opened_cards):
        for player in players:
            d = CheckCombos().number_group(player, opened_cards)
            
            for suit, cards in d.items():
                if len(cards) == 4:
                    print(player.name, 'total cards: ', d)
                    return player.name
        
        return False
    
    def three_of_kind(self, d):
            
        for cards, suit in d.items():
            if len(suit) == 3:
                return True
        
        return False
    def pair(self, d):
            
        for cards, suit in d.items():
            if len(suit) == 2:
                return True
        
        return False
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

    flush = CheckCombos().flush(players, opened_cards)
    if flush:
        print(flush , 'won and had a Flush')
        exit()
    
    for player in players:
        d = CheckCombos().number_group(player, opened_cards)
        player.best_combo = CheckCombos().all_combos(d)
    
    print(players)
    players = sorted(players, key=lambda x: x.best_combo)


    print('the winning player is ', players[0].show_hand())
    if players[0].best_combo == 1:
        print('Four of a Kind')
    elif players[0].best_combo == 2:
        print('Full House')
    elif players[0].best_combo == 3:
        print('Three of a Kind')
    elif players[0].best_combo == 3:
        print('Pair')

    print('Game Over')
if __name__ == '__main__':
    main()