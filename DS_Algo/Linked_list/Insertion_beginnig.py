class Node:
    def __init__(self, v):
        self.value=v
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    
    def insert_begin(self,value):
        new_node=Node(value)
        if self.head==None:
            self.head=new_node 
            self.tail=new_node
        else:
            new_node.next=self.head 
            self.head=new_node

        self.length+=1

    def __str__(self):
        tmp_node=self.head 

        ans=''
        while tmp_node != None:
            ans+=str(tmp_node.value)
            if tmp_node.next != None:
                ans+=' --> '
            tmp_node=tmp_node.next

        return ans


def main():

    k=LinkedList()

    k.insert_begin(4)
    k.insert_begin(3)
    k.insert_begin(2)
    print(k)

if __name__ == '__main__':  
    main()
