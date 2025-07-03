class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        visited = []
        for i in range(n):
                visited.append([False] * m)
        
        # def explore(i, j):
        #     visited[i][j] = True
        #     e1 = e2 = False

            
        #     if i + 1 < n and board[i + 1][j] == 'O' and not visited[i + 1][j]:
        #         e1 = explore(i + 1, j)
                    
        #     if j + 1 < m and board[i][j + 1] == 'O' and not visited[i][j + 1]:
        #         e2 = explore(i, j + 1)
            
        #     if i + 1 == n or j + 1 == m or i == 0 or j == 0:
        #         return True

        #     if e1 or e2:
        #         return True
        #     else:
        #         return False
        

        def capture(i, j, ch):
            board[i][j] = ch
            visited[i][j] = True
            if i < (n-1) and board[i + 1][j] == 'O' and not visited[i + 1][j]:
                capture(i + 1, j, ch)
            if j< (m-1) and board[i][j + 1] == 'O' and not visited[i][j + 1]:
                capture(i, j + 1, ch)
            if i > 0 and board[i - 1][j] == 'O' and not visited[i - 1][j]:
                capture(i - 1, j, ch)
            if j > 0 and board[i][j - 1] == 'O' and not visited[i][j - 1]:
                capture(i, j - 1, ch)
                

        for i in range(n):
            if board[i][0] == 'O' and not visited[i][0]:
                capture(i,0,'S')
            if board[i][m-1] == 'O' and not visited[i][m-1]:
                capture(i,m-1,'S')
        
        for j in range(m):
            if board[0][j] == 'O' and not visited[0][j]:
                capture(0,j,'S')
            if board[n - 1][j] == 'O' and not visited[n - 1][j]:
                capture(n - 1,j,'S')
        
    
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O' and not visited[i][j]:
                    capture(i, j, 'X')


        for i in range(n):
            for j in range(m):
                if board[i][j] == 'S':
                    board[i][j] = 'O'
                     
                    

        

        
        

            