# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = head 
        curr_i = head
        pos_i = 1
        if right - left == 0:
            return head
        
        while pos_i < (left-1):
            prev = prev.next
            pos_i += 1
        print(prev.val)
        
        if left > 1:
            curr_i = prev.next

        curr_j = head 
        pos_j = 1
        while pos_j <= right:
            curr_j = curr_j.next
            pos_j += 1
        
        count = 0
        while count < (right - left):
            next_node = curr_i.next
            front_to_back = ListNode()
            front_to_back.val = curr_i.val
            front_to_back.next = curr_j

            curr_i = next_node
            curr_j = front_to_back
            count += 1

        if prev != curr_i:
            prev.next = curr_i
            curr_i.next = curr_j
        if left == 1:
            prev = prev.next
            return prev
        
        return head




