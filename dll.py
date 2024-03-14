class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class dll:
    def __init__(self):
        self.head=None

    def add_element(self, data):
        k = node(data)
        if self.head is None:
            self.head = k
            return

        left_node = self.head
        while left_node.next is not None:  # Ensure we stop at the last node
            left_node = left_node.next

        left_node.next = k
        k.prev = left_node  # It should be k.prev not k.previous

    def printdll(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def printdll_reverse(self):
        temp=self.head
        while temp:
            k=temp
            temp=temp.next

        while k:
            print(k.data)
            k=k.prev

def main():
    list=dll()
    list.add_element(1)
    list.add_element(2)
    list.add_element(3)
    list.printdll()
    list.printdll_reverse()

if __name__=="__main__":
    main()