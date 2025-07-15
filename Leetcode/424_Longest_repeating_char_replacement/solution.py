class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        n = len(s)
        d = {}
        
        ans = 0 
        max_freq = 0
        while l <= r and r < n:
            d[s[r]] = 1 + d.get(s[r] , 0)
        
            max_freq = max(max_freq, d[s[r]])
            
            if r - l + 1 - max_freq > k:
                d[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
            
        
        return ans

             
s = 'ABBB'
print(Solution().characterReplacement(s , 1))               

            