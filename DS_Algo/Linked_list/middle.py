class Node:
    def __init__(self, v):
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
        

def main():

    k = LinkedList()

    k.insert_begin(4)
    k.insert_begin(3)
    k.insert_begin(2)
    k.insert_end(6)
    print(k)

    print(f"delete {2} position deleted {k.delete(2).value}")
    print(k)
    k.reverse()

    print(k)
    k.middle()
    print(k)

if __name__ == '__main__':  
    main()
