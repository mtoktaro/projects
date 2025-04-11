# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode()
        curr = new_node

        while (list1) and (list2): 
            if list1.val > list2.val:
                curr.next = list2
                list2 = list2.next
                curr = curr.next
                print(curr.val)
            else: 
                curr.next = list1
                list1 = list1.next
                curr = curr.next
                print(curr.val)
        
        if list1 == None: 
            curr.next = list2
        else:
            curr.next = list1

        return new_node.next
