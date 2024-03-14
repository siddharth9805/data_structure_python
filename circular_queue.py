class Circularll:
    def __init__(self,capicity):
        self.capacity=capicity
        self.queue=[None]*capicity
        self.front=self.size=0
        self.rear=capicity-1

    def isFull(self):
        if self.size==self.rear:
            return True
        return False

    def isEmpty(self):
        if self.size==0:
            return True
        return False

    def enqueue(self,data):
        self.rear=(self.rear+1)%self.capacity
        self.queue[self.rear]=data
        self.size+=1

    def dequeue(self):
        iteam=self.queue[self.front]
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return iteam

    def front(self):
        if self.isEmpty():
            return None
        return self.front

    def rear(self):
        if self.isFull():
            return None
        return self.rear()

    def printcq(self):
        for i in range(self.size):
            print(self.queue[self.front+i % self.size], end=' ')

def main():
    cq=Circularll()
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.printcq()

if __name__=='__main__':
    main()