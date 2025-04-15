import random
from matrix import Matrix
from check import Check 

def main():

    n , m, k = map(int, input("Please input board dimensions (n, m) and number of of symbols (k) in a row for the win: ").split())
    print(n, m, k)

    move = False
    
    matrix = Matrix(n, m)
    count = 0
    a = set()
    while move == False:

        correct_move = False
        while correct_move == False:

            p1 = input("Player enter your coordinates: ")

            p1 = p1.split(' ')
            x = int(p1[0])
            y = int(p1[1])
            
            correct_move = matrix.update_matrix(matrix, x, y, n, m, 'X')
        
        count += 1
        a.add((x, y))
            
        if Check.check_bingo(matrix, n, m, k, 'X') == True:
            print('Player won')
    
            return 0
                
        Check.check_final_move(count)
        
        correct_move = False
        print('Dumb Computer move:')
        
        while correct_move == False:
            x = random.randint(0, n - 1)
            y = random.randint(0, m - 1)
            
            correct_move = matrix.update_matrix(matrix, x, y, n, m, 'O')
                
        count+=1
        
        if Check.check_bingo(matrix, n, m, k, 'O') == True:
            print('Computer won')
            move = True
 
        Check.check_final_move(count)


if __name__ == '__main__':
    main()