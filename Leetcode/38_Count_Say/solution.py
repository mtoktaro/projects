class Solution:
    def countAndSay(self, n: int) -> str:
        s = '1'

        for i in range(n-1):
            j = 0
            tmp = ''
            while j < len(s):
                count = 1
                while j + 1 < len(s) and s[j] == s[j + 1]:
                    j += 1 
                    count += 1

                tmp += str(count) + s[j]
                j += 1

            s = tmp
        

        return s
                

            
        