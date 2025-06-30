class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0]*3
        for num in nums:
            if num == 0:
                count[0] += 1
            elif num == 1:
                count[1] += 1
            elif num == 2:
                count[2] += 1
        
        print(count)
        pos = 0
        for i in range(3):
            for j in range(count[i]):
                nums[pos] = i
                pos += 1
