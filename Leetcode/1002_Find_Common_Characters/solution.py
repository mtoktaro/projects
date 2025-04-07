
from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        ans = []
        for i, word in enumerate(words):
            d = Counter(word)
            if i == 0:
                final_d = d
            else: 
                for letter in final_d.keys():
                    final_d[letter] = min(d[letter], final_d[letter])

        for k,v in final_d.items():
            for j in range(v):
                ans.append(k)

        return ans

                


                    
            

            
        