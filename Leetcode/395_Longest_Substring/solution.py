class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def split(l, r, n, s, k):

            d = {}
            for i in range(l, n):
                d[s[i]] = 1 + d.get(s[i], 0)
            
            not_enough_char = set()
            for key, val in d.items():
                if val < k:
                    not_enough_char.add(key)
            if len(not_enough_char) == 0: return n - l  
            
            while r < n:
                if s[r] in not_enough_char:
                    a = split(l, l, r, s, k)
                    b = split(r + 1, r + 1, n, s, k)

                    return max(a, b)
                else:
                    r += 1
            
            


        
        print(split(0, 0, len(s), s, k))


s="ababbc"
k = 2
print(Solution().longestSubstring(s, k))