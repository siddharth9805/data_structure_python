class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None

    def add_node(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node

    def insert_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        self.head=Node(data)
        self.head.next=temp

    def insert_end(self,data):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)

    def insert_after(self,data,nextdata):
        temp=self.head
        k=Node(data)
        while temp.data!=nextdata:
            if temp.next == None:
                return
            temp=temp.next
        k.next=temp.next
        temp.next=k

    def insert_before(self,data,beforedata):
        temp=self.head
        k = Node(data)

        while temp.data!=beforedata:
            if temp.next == None:
                return
            if temp.next.data!=beforedata:
                flag=temp
            temp=temp.next
        k.next=flag.next.next
        flag.next=k

    def printll(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

def main ():
    l=ll()
    l.add_node(1)
    l.add_node(2)
    l.add_node(3)
    l.add_node(4)
    l.insert_begin(10)
    l.insert_end(20)
    l.insert_after(30,3)
    l.insert_before(40, 12)
    l.printll()

if __name__=="__main__":
    main()