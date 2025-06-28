class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path_count = []
        for i in range(m):
            path_count.append([1] * n)
        
        for i in range(1, m):
            for j in range(1, n):
                path_count[i][j] = path_count[i - 1][j] + path_count[i][j - 1]
        
        return path_count[m-1][n-1]

        