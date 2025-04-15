class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        n = len(board)
        m = len(board[0])

        for row in range(len(board)):
            for column in range(len(board[0])):
                if board[row][column] == word[0]:
                    
                    if self.dfs(board, row, column, n, m, 0, set()):
                        return True

        return False

    def dfs(self, board, row, column, n, m, s_pos, visited):
        if s_pos == (len(word) - 1):
            return True
        
        visited.add((row, column))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for dx, dy in directions:
            if (row + dx >= 0) and (row + dx < n) and (column + dy >= 0) and (column + dy < m) and \
               (board[row + dx][column + dy] == word[s_pos + 1]) and ((row + dx, column + dy) not in visited):
        
                if self.dfs(board, row + dx, column + dy, n, m, s_pos + 1, visited):
                    return True

        
        visited.remove((row, column))
        return False
        

        
a = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(Solution().exist(a, word))