class BST:
    def __init__(self):
        self.arr=[None]

    def add(self,data):
        i=0
        while i<len(self.arr):
            if self.arr[i] is None:
                self.arr[i] = data
                return
            if data < self.arr[i]:
                i=2*i+1
            elif data > self.arr[i]:
                i=2*i+2

            while i>=len(self.arr):
                self.arr.append(None)
        self.arr[i]=data

    def search_bst(self, key):
        i = 0  # Start at the root
        while i < len(self.arr) and self.arr[i] is not None:
            if self.arr[i] == key:
                return True
            elif key < self.arr[i]:
                i = 2 * i + 1
            else:
                i = 2 * i + 2
        return False

    def print_bst(self):
        root = self.arr
        print(root)

def main():
    bst=BST()
    bst.add(50)
    bst.add(30)
    bst.add(20)
    bst.add(15)
    bst.add(10)
    bst.add(8)

    print(bst.search_bst(20))

    bst.print_bst()

if __name__=='__main__':
    main()