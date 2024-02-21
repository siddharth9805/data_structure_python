class Queue():
    def __init__(self):
        self.item=[]

    def is_empty(self):
        if len(self.item)==0:
            return True
        else:
            return False

    def add(self,data):
        self.item.append(data)

    def pop(self):
        if self.is_empty():
            raise "Gandu Khali hai"
        else:
            return self.item.pop(0)

    def peek(self):
        if self.is_empty():
            raise "madarchod khali hai"
        else:
            return self.item[0]

def main():
    queue=Queue()
    queue.add(1)
    queue.add(2)
    queue.add(3)

    print(queue.pop())
    print(queue.peek())

if __name__=="__main__":
    main()