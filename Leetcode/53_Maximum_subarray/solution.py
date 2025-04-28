class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        max_iter = [0] * n
        curr = 0
        ans = nums[0]
        negatives = float('-inf')
        for i in range(n):
            negatives = max(negatives, nums[i])
            if (max_iter[i-1] + nums[i]) < 0:
                max_iter[i] = 0
            else:
                max_iter[i] = max_iter[i-1] + nums[i]
            
            ans = max(ans, max_iter[i], nums[i])
        
        if negatives < 0:
            return negatives
        else: 
            return ans 

nums = [-2]


print(Solution().maxSubArray(nums))