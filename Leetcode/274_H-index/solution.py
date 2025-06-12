class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse = True)
        print(citations)
        ans = 0
        for i, citation in enumerate(citations):
            
            if (i+1) <= citation:
                ans = max(ans, i + 1)
                

        return ans

        
        