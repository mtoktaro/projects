class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        curr = head
        s = set(nums)
        ans = 0

        while curr is not None:
            if curr.val in s:
                ans += 1
                curr = curr.next
                  
                while curr is not None and curr.val in s:
                    curr = curr.next
            else:
                curr = curr.next
        
        return ans 