class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        ans = 0
        max_p = 0
        for i in range(n-1,-1, -1):
            ans = max(max_p - prices[i], ans)
            max_p = max(max_p, prices[i])

   
         
        return ans
