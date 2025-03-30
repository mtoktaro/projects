class Node:
    def __init__(self, v = 0):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tmp_node = self.head
        ans = ''

        while tmp_node is not None:
            ans += str(tmp_node.value)
            if tmp_node.next is not None:
                ans += ' --> '
            tmp_node = tmp_node.next

        return ans

    def insert_begin(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert_end(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def delete(self, index):
        tmp = self.head

        if index < 0 or index >= self.length:
            return None

        for _ in range(index-1):
            tmp = tmp.next

        if index == 0:
            self.head = self.head.next
            self.length -= 1

            return tmp
        elif (index + 1) == self.length:
            ans = self.tail
            tmp.next = None
            self.tail = tmp
            self.length -= 1
            return ans
        elif tmp != self.tail:
            ans = tmp.next
            tmp.next = tmp.next.next
            self.length -= 1

            return ans

    def reverse(self):
        prev = None
        curr = self.head
        self.head = self.tail
        self.tail = None
        next = Node(None)

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

    def middle(self):
        if self.length % 2 == 0:
            pos = (self.length/2) + 1
        else:
            pos = (self.length+1) / 2

        curr = self.head
        i = 1

        while i != pos:

            curr = curr.next
            i += 1

        curr.next = None
        self.head = curr

        return curr
        
    def remove_duplicates(self):
        if self.head is None:
            return
        s = set()
        curr = self.head
        s.add(curr.value)
        while curr.next is not None and curr is not None:
            
            while curr.next.value in s:
                curr.next = curr.next.next
                if curr.next is None:
                    return 
                

            s.add(curr.next.value)
            curr=curr.next

    def mergeTwoLists(self, l1, l2):
    # :type list1: Optional[ListNode]
    # :type list2: Optional[ListNode]
    # :rtype: Optional[ListNode]
    
        ll1 = l1.head
        ll2 = l2.head
        new_node = Node()
        
        while (ll1 is not None) and (ll2 is not None): 
            if ll1.value < ll2.value: 
                new_node.next = ll1
                new_node = new_node.next
                ll1 = ll1.next
            else:
                new_node.next = ll2
                new_node = new_node.next
                ll2 = ll2.next
            
        if ll1 is None: 
            new_node.next = ll2
        else: 
            new_node.next = ll1


        if l1.head.value < l2.head.value:
            return l1
        else:
            return l2
        


def main():

    ll = LinkedList()

    ll.insert_begin(1)
    ll.insert_end(7)
    ll.insert_end(7)
    print(ll)

    k = LinkedList()

    k.insert_begin(4)
    k.insert_begin(4)
    k.insert_begin(4)
    k.insert_end(6)
    k.insert_end(6)
    print(k)
    # print(f"delete {2} position deleted {k.delete(2).value}")
    
    # k.reverse()

    ans = LinkedList()
    print(ans.mergeTwoLists(k, ll))
    # k.middle()
   
    print(ans)

if __name__ == '__main__':  
    main()
