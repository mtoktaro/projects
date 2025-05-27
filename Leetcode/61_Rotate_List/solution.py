# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr != None:
            n += 1
            curr = curr.next
        
        if n == 0 or k == 0 or n == k or n == 1:
            return head
            
        if n < k:
            k = k % n
        
        if n == 0 or k == 0 or n == k or n == 1:
            return head
        print(k)
        pos = n - k 
        i = 1
        curr = head
        while i < pos:
            curr = curr.next
            i += 1
        
        new_head = curr.next
        curr.next = None
        tmp = new_head
        while tmp.next != None:
            tmp = tmp.next
        
        tmp.next = head

        return new_head
        