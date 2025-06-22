class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        removals_left = k
        stack = []
        if k == len(num):
            return '0'
        for i in range(n):
            
            while stack and num[i] < stack[-1] and removals_left > 0:
                stack.pop()
                removals_left -= 1
            
            stack.append(num[i])
         
        for i in range(removals_left):
            stack.pop()
        
        ans = ''.join(stack)
        ans = ans.lstrip('0')
        if len(ans) == 0:
            return '0'
        else:
            return ans


