class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        if obstacleGrid[n-1][m-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        for i in range(0, n):
            for j in range(0, m):
                if (i == 0 and j == 0): continue
                elif obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
                    continue
                else:
                    up = left = 0
                    if i > 0 and obstacleGrid[i - 1][j] != -1:
                        up = obstacleGrid[i - 1][j]
                    
                    if j > 0 and obstacleGrid[i][j - 1] != -1:
                        left = obstacleGrid[i][j - 1]
                    
                    obstacleGrid[i][j] = up + left
                
        return obstacleGrid[n-1][m-1]
