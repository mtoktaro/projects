class Check:
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
    
    def check_final_move(count):

        if count==9:
            print('Draw')
            exit()

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
            if Check.check_diagonal(matrix, i, 0, 1, n, m, k, ch) or Check.check_diagonal(matrix, i, m-1, -1, n, m, k, ch):
                return True

        for j in range(m):
            if Check.check_diagonal(matrix, 0, j, 1, n, m, k, ch) or Check.check_diagonal(matrix, 0, m-1, -1, n, m, k, ch):
                return True

        return False