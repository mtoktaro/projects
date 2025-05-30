class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set()
        max = 0
        for word in wordDict:
            word_set.add(word)
            if len(word) > max:
                max = len(word)
        
        order = []
        order.append(0)
        curr = 0
        visited = set()
        while curr < len(order): 

            start = order[curr]
            for i in range(start, start+max+1):
                if i in visited:
                    continue
                if s[start:i] in word_set:
                    order.append(i)
                    visited.add(i)
                    if i == len(s):
                        return True
            
            curr += 1
        
        return False
        

            