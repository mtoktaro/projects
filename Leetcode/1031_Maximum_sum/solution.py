class Solution:
    def longestConsecutive(self, nums) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = (0, False)

        i = 0
        max = 0
        while i < len(nums):
            count = 0
            k = nums[i]
            
            if d[k][1] == True: 
                i += 1 
                continue
            
            
            while (k in d) and d[k][1] == False:
                count += 1
                d[k] = (count, True)
                k += 1
            if (k) in d:
                count += d[k][0]
            d[nums[i]] = (count, True)
            i += 1
            if max < count:
                max = count
         
        return max

def main():
    l = [1, 0, 1, 2]
    
    solution = Solution()
    print(solution.longestConsecutive(l))

if __name__ == '__main__':
    main()