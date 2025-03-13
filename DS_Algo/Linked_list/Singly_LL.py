class Node:
    def __init__(self, v):
        self.value=v
        self.next=None

class LinkedList:
    def __init__(self, value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1



def main():
    


    

    


    k=LinkedList(3)
    print(k)

if __name__ == '__main__':  
    main()
