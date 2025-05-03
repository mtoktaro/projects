class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        n = len(gas)
        diff = [0] * n
        sum = 0
        for i in range(n):
            diff[i] = gas[i] - cost[i]
            sum += diff[i]
        if sum < 0:
            return -1
            
        sum = 0
        max = 0
        current_sum = 0
        total_sum = 0
        ans = 0
        for i in range(n*2):
            current_sum += diff[i % n]
            total_sum += diff[i % n]
            if current_sum < 0:
                current_sum = 0
                ans = (i + 1) % n
                
        if total_sum >= 0 and ans < n:
            return ans
        else:
            return -1
    
 
gas = [5,8,2,8]
cost = [6,5,6,6]

print(Solution().canCompleteCircuit(gas, cost))