class Solution:
    def checkValidString(self, s: str) -> bool:
        pattern = []
        l = -1
        open_br = []
        for i, str in enumerate(s):
            if str == '(':
                pattern.append(str)
                l = len(pattern) - 1
                open_br.append(l)
            elif str == '*':
                pattern.append(str)
            elif str == ')':
                if l >= 0:
                    pattern.pop(l)
                    open_br.pop(-1)
                    if len(open_br) > 0:
                        l = open_br[-1]
                    else:
                        l = -1
                elif len(pattern) > 0 and pattern[-1] == '*':
                    pattern.pop(-1)
                else:
                    return False
        
        ans = 0

        print(pattern)
        for i in pattern:
            if i == '*' and ans > 0:
                ans -= 1
            elif i == '(':
                ans += 1
        
        if ans == 0:
            return True
        else:
            return False




        