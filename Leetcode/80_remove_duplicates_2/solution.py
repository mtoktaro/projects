class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d_count = {}
        k = 0
        for num in nums:
            d_count[num] = d_count.get(num, 0) + 1
            if d_count[num] <= 2:
                nums[k] = num
                k += 1
        
        return k

        