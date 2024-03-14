class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class doublell:
    def __init__(self):
        self.head=None

    def add(self,data):
        if self.head is None:
            self.head=Node(data)
            return

        node=Node(data)

        if node.data < self.head.data:
                node.next = self.head
                self.head.prev = node
                self.head = node
        else:
            temp = self.head
            while temp.next:
                if node.data<temp.next.data:
                    node.prev=temp.next.prev
                    temp.next.prev = node
                    node.next=temp.next
                    temp.next=node
                    break
                else:
                    temp=temp.next

            if temp.next is None:
                temp.next = node
                node.prev = temp


    def queue_length(self):
        length=0
        current=self.head
        while current:
            current=current.next
            length+=1

        return length

    def is_queue_empty(self):
        if self.queue_length()==0:
            return True
        return False

    def pop(self):
        temp=self.head
        if self.is_queue_empty():
            return None

        while temp.next.next:
            temp=temp.next

        data=temp.next.data
        temp.next=temp.next.next

        return data
    def printdll(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print()

    def printdllrev(self):
        temp=self.head
        while temp.next:
            temp=temp.next
        print()
        while temp:
            print(temp.data, end=' ')
            temp=temp.prev

def main():
    dll=doublell()
    dll.add(4)
    dll.add(2)
    dll.add(3)
    dll.add(1)
    dll.add(9)
    dll.add(6)
    dll.add(5)
    dll.printdll()
    dll.printdllrev()

if __name__=="__main__":
    main()