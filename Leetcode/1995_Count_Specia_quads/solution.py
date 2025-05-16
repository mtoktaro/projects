class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n-3):
            for j in range(n-1, 2, -1):
                for k in range(i+1, j):
                    for l in range(k+1, j):
                        if nums[i] == (nums[j]-nums[k]-nums[l]):
                            ans+=1

 
        return ans
        