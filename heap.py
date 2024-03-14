class Heap:
    def __init__(self):
        self.heap=[]

    def parent(self,index):
        return (index-1)// 2

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

    def delete(self,length):
        root = self.heap[0]
        self.heap[0]=self.heap[length]
        self.heap.pop(length)
        self.heapifydown(0,length)
        self.heap.append(root)
        return root

    def sort(self):
        length = len(self.heap)

        while length > 0:
            self.delete(length - 1)
            length = length - 1

    def heapifydown(self,index,length):
        small=index
        left=self.leftchild(index)
        right=self.rightchild(index)
        if left<length and self.heap[left]<self.heap[small] and self.heap[left]<self.heap[right]:
            small=left
        elif right<length and self.heap[right]<self.heap[small] and self.heap[right]<self.heap[left]:
            small=right

        if small!=index:
            if self.heap[small]<self.heap[index]:
                self.heap[small],self.heap[index]=self.heap[index],self.heap[small]
            self.heapifydown(small,length)

    def min_value(self):
        return self.heap[0]

def main():
    heap=Heap()

    arr=[10,20,15,12,40,25,18]
    for item in arr:
        heap.add(item)

    print("Original Heap")
    print(heap.heap)

    heap.sort()

    print("\nSorted Heap")
    print(heap.heap)

if __name__=='__main__':
    main()