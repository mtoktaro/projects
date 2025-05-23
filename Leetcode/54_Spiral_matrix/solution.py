class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        m = len(matrix[0])
        ans = []
        visited = []
        for i in range(n):
            visited.append([-1000]*m)

        count = 1
        i = 0
        j = 0
        while visited[i][j] == -1000:
            while j < m and visited[i][j] == -1000:
                visited[i][j] = matrix[i][j]
                ans.append(matrix[i][j])
                
                count += 1
                j += 1
            print(ans)
            print('hi')
            j-=1
            i+=1
            if count > (n * m):
                break
            while i < n and visited[i][j] == -1000:
                visited[i][j] = matrix[i][j]
                ans.append(matrix[i][j])
                
                count += 1
                i += 1
            print(ans)
            print('hi')
            i -= 1
            j -= 1
            if count > (n * m):
                break
            while j >=0 and visited[i][j] == -1000:
                visited[i][j] = matrix[i][j]
                ans.append(matrix[i][j])
                
                count += 1
                j -= 1
            print(ans)
            print('hi')
            j += 1
            i -= 1
            if count > (n * m):
                break
            while i >=0 and visited[i][j] == -1000:
                visited[i][j] = matrix[i][j]
                ans.append(matrix[i][j])
                count += 1
                i -= 1
            i += 1
            j += 1
            print(visited)
            print(i, ' ', j)
            print('hi')
        
      
        return ans
        