class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        
        max_num = 0
        min_num = float('inf')
        nums_set = set(nums)
        for num in nums_set:
            max_num = max(max_num, num)
            min_num = min(min_num, num)

        if len(nums_set) < 2 or max_num == min_num:
            return 0
        
        group_spread = (max_num - min_num) // len(nums_set)
        if group_spread == 0:
            return 1

        groups = []
        group_count = (max_num - min_num) // group_spread
        for i in range(group_count + 1):
            groups.append([None, None])
        print(groups)

        for num in nums_set:
            i = (num - min_num) // group_spread
            print(i)
            if groups[i][0] == None:
                groups[i][0] = num
                groups[i][1] = num
            else:
                groups[i][0] = min(groups[i][0], num)
                groups[i][1] = max(groups[i][1], num)
        
        prev_max = -1
        ans = 0
        for i in range(len(groups)):
            if groups[i][0] != None:
                if prev_max != -1:
                    ans = max(ans, groups[i][0] - prev_max)
                prev_max = groups[i][1]
            
        
        return ans

        