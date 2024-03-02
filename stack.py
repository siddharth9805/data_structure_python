class Stack:
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
            raise "empty"
        return self.item.pop()

    def length(self):
        return len(self.item)

    def peek(self):
        if self.is_empty():
            raise "empty"
        else:
            return self.item[-1]

def main():
    stack=Stack()
    stack.add(1)
    stack.add(2)
    stack.add(3)
    print(stack.pop())
    print(stack.peek())

if __name__=="__main__":
    main()