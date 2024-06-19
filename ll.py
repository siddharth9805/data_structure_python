class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class ll:
    def __init__(self):
        self.head=None
        self.length = 0

    def add_node(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return

        temp=self.head

        while temp.next is not None:
            temp=temp.next

        temp.next=new_node
        self.length+=1

    def insert_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        temp=self.head
        self.head=Node(data)
        self.head.next=temp
        self.length += 1

    def insert_end(self,data):
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=Node(data)
        self.length += 1

    def insert_after(self,data,nextdata):
        temp=self.head
        k=Node(data)
        while temp.data!=nextdata:
            if temp.next == None:
                return
            temp=temp.next
        k.next=temp.next
        temp.next=k
        self.length += 1

    def del_node_begin(self):
        if self.head is None:
            return

        temp=self.head
        item = temp.data
        self.head=temp.next
        del(temp)
        self.length -= 1
        return item

    def reverse(self):
        previous = None
        current = self.head
        while current:
            next_temp = current.next  # Save next node
            current.next = previous  # Reverse current node's pointer
            previous = current  # Move pointers one step forward
            current = next_temp
        self.head = previous  # New head of the reversed list

    def duplicatefromUnsort(self):
        temp=self.head
        i=0
        while temp:
            k=temp
            while k.next:
                if temp.data==k.next.data:
                    k.next=k.next.next
                else:
                    k=k.next
                    i+=1
            temp=temp.next

    def lastnodetofirst(self):
        temp=self.head
        while temp.next.next:
            temp=temp.next
            k=temp

        lastnode=k.next
        k.next=None

        lastnode.next=self.head
        self.head=lastnode

    def middleoflinklist(self):
        temp=self.head
        k=0

        while k!=self.length//2:
            temp=temp.next
            k+=1

        return temp.data

    def deletegreatevalue(self):
        temp=self.head

        while temp.next:
            if temp.data<temp.next.data:
                temp.data=-1
            temp=temp.next

        temp=self.head

        while temp.data ==-1:
            temp=temp.next

        self.head=temp

        while temp.next:
            if temp.next.data ==-1:
                temp.next=temp.next.next
            temp=temp.next

    def cyclic_detection(self):
        fast=self.head
        slow=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow==fast:
                return True

        return False

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
        self.length += 1

    def swap_node(self):
        self._swap_node(self.head,0)

    def _swap_node(self,head,j):
        if head is None:
            return
        current = head
        temp = current.next
        k = temp.next
        temp.next = current
        if j==0:
            self.head=temp
        current.next = self._swap_node(k,1)
        return temp

    def rotate(self,k):
        start=self.head
        current=self.head
        temp=self.head
        initial_point=0

        while temp.next:
            temp=temp.next

        temp.next=start

        while initial_point!=self.length-k:
            current=current.next
            initial_point+=1

        self.head=current.next
        current.next=None

    def duplicate(self):
        current=self.head
        while current.next:
            temp=current.next
            if current.data==temp.data:
                current.next=current.next.next
            else:
                current=current.next

    def partition(self,x):
        self._partition(self.head,x)

    def  _partition(self,current,x):
        temp=current.next
        k=temp
        while temp:
            if temp.next.data <x:
                l=temp.next
                temp.next=temp.next.next
                current.next=l
                current=current.next
                l.next=k
            temp=temp.next

    def reorder_list(self):
        temp=self.head

        while temp:
            k=temp.next
            if k is None or k.next is None:
                return
            while k.next.next:
                k=k.next
            l=temp.next
            temp.next=k.next
            k.next=None
            temp.next.next=l
            temp=temp.next.next

    def cyclicFinder(self):
        fast = self.head
        slow = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

            slow=self.head
            if slow!=fast:
                slow=slow.next
                fast=fast.next

        return slow

    def reverse_recursion(self):
        length=0
        temp=self.head
        while temp:
            length+=1
            temp=temp.next

        self._reverse(self.head,length)

    def _reverse(self,root,length):
        if length==0:
            return
        k=root
        count=0
        while count<length-1:
            root=root.next
            count+=1
        k.data,root.data=root.data,k.data
        k=k.next
        return self._reverse(k,length-2)

    def printll(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        print()

def main ():
    l=ll()
    l.add_node(1)
    l.add_node(2)
    l.add_node(3)
    l.add_node(4)
    l.add_node(5)
    l.add_node(6)
    l.printll()
    l.swap_node()
    l.printll()

if __name__=="__main__":
    main()