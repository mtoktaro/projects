import heapq 

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        ans = []
        for i, num in enumerate(nums):
            
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            dq.append(i)            
            if dq[0] == (i-k):
                dq.popleft()
            
            if i >= (k-1):
                ans.append(nums[dq[0]])

        return ans
nums = [1,3,-1,-3,5,3,6,7]
k = 3

print(Solution().maxSlidingWindow(nums, k))

