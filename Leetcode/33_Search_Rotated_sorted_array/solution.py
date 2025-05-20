class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1
        while l < r: 
            m = (l+r) // 2
            # print(l,' ', r, ' ', m)
            if nums[l] < nums[r]:
                break
            if nums[m] > nums[r]:
                l = m + 1
            else:
                l += 1

        rr = l
        ll = 0
        while l < r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m
            elif nums[m] == target:
                return m
        
        if nums[l] == target:
            return l
        
        while ll < rr:
            m = (ll + rr) // 2
            if nums[m] < target:
                ll = m + 1
            elif nums[m] > target:
                rr = m
            elif nums[m] == target:
                return m
        
        if nums[ll] == target:
            return ll
        
        return -1
