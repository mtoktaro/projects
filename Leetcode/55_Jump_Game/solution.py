class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        n = len(nums)
        if n ==1 : return True
        d = {} 
        for i in range(n-1):
            if nums[i] !=0:
                d[i] = i + nums[i]
            
        path = []
        path.append(0)
        i = 0 
        while i < len(path):
            print(i)

            if path[i] in d:
                for j in range(path[i] + 1, path[i] + d[path[i]]+1):
                    if j in d:
                        print(j, d[j])
                        path.append(j)
                        if d[j] == (n-1):
                            return True
                    if j == (n-1):
                        return True
                print(path)
            i += 1
        
        return False

l = [3,2,1,0,4]

print(Solution().canJump(l))