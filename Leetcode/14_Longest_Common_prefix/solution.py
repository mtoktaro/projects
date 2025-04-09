class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''        
        for i in range (len(strs[0])):
            count = 1
            letter = strs[0][i]

            for j in range (1,len(strs)):
                word = strs[j]
                if (len(ans) + 1) <= len(word) and word[i] == letter:
                    print(word[i])
                    count += 1
                    
            if count == len(strs):
                ans += letter
            else:
                break
                 
        
        return ans 