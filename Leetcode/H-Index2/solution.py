class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        l = 0
        n = len(citations)
        r = n - 1
        if max(citations) > 0:
            ans = 1
        else:
            ans = 0

        while l < r:
            m = (l + r) // 2
            
            if citations[m] >= (n - m):
                ans = max(ans, n - m) 
                
            if citations[m] > (n - m):
                r = m
            else:
                l = m + 1

        return ans
        