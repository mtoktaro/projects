class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.best_combo = 100
        self.highest_card = 0.0
    
    def add_card(self, card):
        self.hand.append(card)
    
    def show_hand(self):
        return self.name, self.hand, self.best_combo, self.highest_card
        