class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        l,r,n = 0,k,len(nums)
        s = set()
        d = {}
        sum = 0
        max_freq = 0
        ans = 0
        for i in range(k):
            sum += nums[i]
            # s.add(nums[i])
            d[nums[i]] = 1 + d.get(nums[i], 0)
        
        if len(d) == k:
            ans = sum

        while r < n:
            sum = sum - nums[l] + nums[r]
            d[nums[r]] = 1 + d.get(nums[r], 0)
            d[nums[l]] -= 1
            if d[nums[l]] == 0:
                del d[nums[l]]

            if len(d) == k:
                ans = max(ans, sum)
            
            l+=1
            r+=1
            

 
        
        return ans
    
l = [1,9,9]


ans=Solution().maximumSubarraySum(l, 2)
print(ans)