class Matrix:
    def __init__(self, height, width):
        self.val = [['.'] * height for i in range(width)]
    
    def update_matrix(matrix, x, y, n, m, ch):

        if matrix[x][y] == '.' and x < n and y < m and x >= 0 and y >= 0:

            matrix[x][y] = ch
            for i in matrix:
                print(i)
            
            return True

        return False