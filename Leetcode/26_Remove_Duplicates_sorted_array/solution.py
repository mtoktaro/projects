class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        pos = 0
        s = set()
        n = len(nums)
        while i < n:
            while i < n and nums[i] in s:
                print(nums[i])
                i += 1
            
            if i < n:
                s.add(nums[i])
                nums[pos] = nums[i]
                pos += 1
                i += 1
            
        
        return len(s)
        

        