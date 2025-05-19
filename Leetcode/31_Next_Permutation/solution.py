class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n-1

        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        
        if i == 0:
            nums.reverse()
            return 
        
        pos = 0
        min = float('inf')
        for j in range(i, n):
            print(nums[j])
            if min > nums[j] and nums[j]>nums[i-1]:
                min = nums[j]
                pos = j
        
        tmp = nums[i-1]
        nums[i-1] = nums[pos]
        nums[pos] = tmp

        nums[i:] = sorted(nums[i:])
        
