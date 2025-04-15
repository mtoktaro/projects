import random
class Matrix:
    def __init__(self, width, height):
        self.val = [['.'] * height for i in range(width)]
    
    

def check_final_move(count):

    if count==9:
        print('Draw')
        exit()

def update_matrix(matrix, x, y, n, m, ch):

    if matrix[x][y] == '.' and x < n and y < m and x >= 0 and y >= 0:

        matrix[x][y] = ch
        for i in matrix:
            print(i)
        
        return True

    return False

def check_diagonal(matrix, x, y, pos, n, m, k, ch):
    
    counter = 0
    while x < n and y < m: 
        
        if matrix[x][y] == ch:
            counter += 1
        else:
            counter = 0
        
        if counter == k:
            return True
        
        x += 1
        y += pos
    return False

def check_bingo(matrix, n, m, k, ch):

    for i in range(n):
        x_counter = 0
        y_counter = 0

        for j in range(m):
            if matrix[i][j] == ch:
                x_counter += 1
            else: 
                x_counter = 0
            
            if matrix[j][i] == ch:
                y_counter += 1
            else: 
                y_counter = 0
            
            if y_counter == k or x_counter == k: 
                return True
    
    for i in range(n):
        if check_diagonal(matrix, i, 0, 1, n, m, k, ch) or check_diagonal(matrix, i, m-1, -1, n, m, k, ch):
            return True

    for j in range(m):
        if check_diagonal(matrix, 0, j, 1, n, m, k, ch) or check_diagonal(matrix, 0, m-1, -1, n, m, k, ch):
            return True

    return False

def main():

    n , m, k = map(int, input("Please input board dimensions (n, m) and number of of symbols (k) in a row for the win: ").split())
    print(n, m, k)

    move = False
    
    matrix = [['.'] * n for i in range(m)]
    count = 0
    a = set()
    while move == False:

        correct_move = False
        while correct_move == False:

            p1 = input("Player enter your coordinates: ")

            p1 = p1.split(' ')
            x = int(p1[0])
            y = int(p1[1])
            
            correct_move = update_matrix(matrix, x, y, n, m, 'X')
        
        count += 1
        a.add((x, y))
            
        if check_bingo(matrix, n, m, k, 'X') == True:
            print('Player won')
    
            return 0
                
        check_final_move(count)
        
        correct_move = False
        print('Dumb Computer move:')
        
        while correct_move == False:
            x = random.randint(0, n - 1)
            y = random.randint(0, m - 1)
            
            correct_move = update_matrix(matrix, x, y, n, m, 'O')
                
        count+=1
        
        if check_bingo(matrix, n, m, k, 'O') == True:
            print('Computer won')
            move = True
 
        check_final_move(count)


if __name__ == '__main__':
    main()