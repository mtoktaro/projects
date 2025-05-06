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
        
    def flush(self, d):
        for suit, cards in d.items():
            if len(cards) == 5:
                return True
        
        return False

    def four_of_kind(self, d):
        for cards, suit in d.items():
            if len(suit) == 4:
                return True
        
        return False
    
    def three_of_kind(self, d):
        for cards, suit in d.items():
            if len(suit) == 3:
                return True
        
        return False
    def pair(self, d):
        counter = 0
        max_pair = 0
        for cards, suit in d.items():
            if len(suit) == 2:
                counter += 1
                max_pair = max(max_pair, cards)
        
        return counter, max_pair

    def pair_value(self, pairs, max_pair):
        if pairs == 2:
            return float(5 + (100 - max_pair) / 100)
        if pairs == 1:
            return float(6 + (100 - max_pair) / 100)

    def all_combos(self, d_numbers, d_suits):
        
        pairs, max_pair = CheckCombos().pair(d_numbers)
        if CheckCombos().flush(d_suits):
            return 1.0
        if CheckCombos().four_of_kind(d_numbers):
            return 2.0
        elif CheckCombos().three_of_kind(d_numbers) and max(CheckCombos().pair(d_numbers)):
            return 3.0
        elif CheckCombos().three_of_kind(d_numbers):
            return 4.0
        elif pairs >= 1:
            return CheckCombos().pair_value(pairs, max_pair)
        
        return 7.0
    
    