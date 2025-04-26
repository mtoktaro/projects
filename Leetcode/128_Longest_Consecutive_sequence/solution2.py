class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set()
        ans = 0
        l = []
        for i in nums:
            sett.add(i)

        for i in sett:
            if i-1 not in sett:
                l.append(i)

        for i in l:
            k = i
            length = 0
            while k in sett:
                length += 1
                k += 1  
            ans = max(ans, length)
        return ans
     
l = [100,4,200,1,3,2]

print(Solution().longestConsecutive(l))