class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        if n < 3:
            return max(nums)

        robbed = []
        ans = 0
        for i in range(n):
            if i < 2:
                robbed.append(nums[i]) 
            elif i == 2:
                robbed.append(nums[i] + robbed[i-2])
            else:
                robbed.append(nums[i]+max(robbed[i-2], robbed[i - 3]))
            
            if ans < robbed[i]:
                ans = robbed[i]

        return ans
        


        