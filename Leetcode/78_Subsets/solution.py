class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def subset(curr, pos):
            ans.append(curr.copy())

            for i in range(pos, len(nums)):
                curr.append(nums[i])
                subset(curr, i+1)
                curr.pop()
            

        subset([], 0)

        return ans
        