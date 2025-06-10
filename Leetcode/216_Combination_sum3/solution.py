class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def combos(curr, number, total, sum):
            
            if sum > total or len(curr) > k:
                return 
            elif sum == total and len(curr) == k:
                ans.append(curr[:])
                
            
            

            for i in range(number, 10):
                if sum + i > n:
                    return 
                else:
                    
                    curr.append(i)
                    combos(curr, i + 1, total, sum + i)
                    curr.pop()


        combos([], 1, n, 0)

        return ans
