class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        n = len(matrix[0])
        row = [0] * n
        
        while count < n**2:
            count += 1
            min_num = float('inf')
            for i, j in enumerate(row):
                
                if i>=0 and i<n and j>=0 and j<n and min_num > matrix[i][j]:
                    min_num = matrix[i][j]
                    pos_i = i
                    pos_j = j
            
            print(min_num)
            
            if count == k:
                return matrix[pos_i][pos_j]
            else:
                row[pos_i] += 1
            

        