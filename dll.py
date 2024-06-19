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

        if data<self.head.data:
            k.next=self.head
            self.head.prev=k
            self.head=k

        curr=self.head
        while curr and data>curr.data:
            prev=curr
            curr=curr.next

        temp=prev.next
        prev.next=k
        k.prev=prev
        k.next=temp

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
    list.add_element(5)
    list.add_element(9)
    list.add_element(7)
    list.printdll()
    # list.printdll_reverse()

if __name__=="__main__":
    main()