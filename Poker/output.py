class Output:
    def print(self, players):
        for i in players:
            print('Players cards: ', i.show_hand())

        print('The winning player is ', players[0].show_hand())
        if players[0].best_combo == 1.0:
            print('Flush')
        elif players[0].best_combo == 2.0:
            print('Four of a Kind')
        elif players[0].best_combo == 3.0:
            print('Full House')
        elif players[0].best_combo == 4.0:
            print('Three of a Kind')
        elif (players[0].best_combo >= 5.0) and (players[0].best_combo < 6.0):
            print('Two Pairs')
        elif (players[0].best_combo >= 6.0) and (players[0].best_combo < 7.0):
            print('Pair')
        else:
            print('High Card')

        print('Game Over')