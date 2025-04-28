class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = 0
        ans = [0]*len(temperatures)
        for i in range(len(temperatures)):
            n = len(stack)
            while n>0 and stack[n-1][0] < temperatures[i]:
                t,r = stack.pop()
                # print('remove: ',t,r)
                ans[r] = (i-r)
                n = len(stack)


            if i == 0 or n == 0 or stack[n-1][0] >= temperatures[i]:
                stack.append((temperatures[i], i))
                # print('append: ',temperatures[i], i)
            
        
        
        return ans
    
temperatures = [73,74,75,71,69,72,76,73]

print(Solution().dailyTemperatures(temperatures))
