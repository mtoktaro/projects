class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        
        for i in range(n):
            pos = len(stack)
            if s[i] in ('(','[', '{'):
                stack.append(s[i])
                continue

            if s[i] == ')':
                if pos > 0 and stack[pos - 1] == '(':
                    stack.pop(pos - 1)
                else:
                    
                    return False
            
            if s[i] == ']':
                if pos > 0 and stack[pos - 1] == '[':
                    stack.pop(pos - 1)
                else:
                    return False

            if s[i] == '}':
                if pos>0 and stack[pos - 1] == '{':
                    stack.pop(pos - 1)
                else:
                
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False



print(Solution().isValid("()[]{}"))