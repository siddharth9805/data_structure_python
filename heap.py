class Heap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return index // 2

    def leftchild(self,index):
        return 2*index+1

    def rightchild(self,index):
        return 2*index+2

    def add(self,data):
        self.heap.append(data)
        self.heapifyup(len(self.heap)-1)

    def heapifyup(self,index):
        while index>0 and self.heap[index]<self.heap[self.parent(index)]:
            self.heap[index],self.heap[self.parent(index)]=self.heap[self.parent(index)],self.heap[index]

            index=self.parent(index)

    def delete(self):
        self.heap[0]=self.heap[-1]
        root=self.heap.pop()
        self.heapifydown(0)
        return root

    def heapifydown(self,index):
        small=index
        right=self.rightchild(index)
        left=self.leftchild(index)
        length=len(self.heap)
        if left<length and self.heap[left]<self.heap[small]:
            small=left
        elif right<length and self.heap[right]<self.heap[small]:
            small=right

        if small != index:
            self.heap[index],self.heap[small]=self.heap[small],self.heap[index]
            self.heapifydown(small)

    def min_value(self):
        return self.heap[0]

def main():
    heap=Heap()
    heap.add(10)
    heap.add(20)
    heap.add(15)
    heap.add(12)
    heap.add(40)
    heap.add(25)
    heap.add(18)

    print(heap.heap)
    print(heap.delete())
    print(heap.heap)

if __name__=='__main__':
    main()