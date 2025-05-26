class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key = lambda x : x[0])
        
        max = float('-inf')
        min = intervals[0][0]
        ans = []
        for interval in intervals:
            if abs(max) >= interval[0] and max < interval[1]:
                max = interval[1]
            elif max < interval[0]:
                ans.append([min, max])
                min = interval[0]
                max = interval[1]
        
        ans.append([min, max])

        return ans
            



            