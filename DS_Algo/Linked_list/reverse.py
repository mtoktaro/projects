class Node:
    def __init__(self, v):
        self.value=v
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def __str__(self):
        tmp_node=self.head 

        ans=''
        while tmp_node != None:
            ans+=str(tmp_node.value)
            if tmp_node.next != None:
                ans+=' --> '
            tmp_node=tmp_node.next

        return ans
    
    def insert_begin(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node 
            self.tail=new_node
        else:
            new_node.next=self.head 
            self.head=new_node

        self.length+=1
    
    def insert_end(self, value):
        new_node=Node(value)
        if self.head == None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def delete(self, index):
        tmp=self.head
        if index<0 or index>=self.length:
            return None

        for _ in range(index-1):
            tmp=tmp.next
        
        if index == 0:
            self.head=self.head.next
            self.length-=1
            return tmp
        elif (index+1)==self.length:
            ans=self.tail
            tmp.next=None
            self.tail=tmp
            self.length-=1
            return ans
            
        elif tmp!=self.tail:
            ans=tmp.next
            tmp.next=tmp.next.next
            self.length-=1
            return ans
    
    def reverse(self):
        



def main():

    k=LinkedList()

    k.insert_begin(4)
    k.insert_begin(3)
    k.insert_begin(2)
    k.insert_end(6)
    print(k)


    print(f"delete {2} position deleted {k.delete(2).value}")
    print(k)
    k.reverse()

    print(k)
if __name__ == '__main__':  
    main()
