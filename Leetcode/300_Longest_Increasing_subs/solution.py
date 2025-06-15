class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        max_length = [0] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    max_length[i] = max(max_length[i], max_length[j] + 1)
            
            if ans < max_length[i]:
                ans = max_length[i]
        
        
        return ans+1

