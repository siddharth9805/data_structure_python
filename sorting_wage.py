class Sort:
    def __init__(self,arr_items):
        self.arr=arr_items

    def selection(self):
        return self._selection(self.arr,0)

    def _selection(self,arr,pointer):
        if pointer==len(arr):
            return 
        min=arr[pointer]
        index=pointer
        j=pointer+1

        while j<len(arr):
            if arr[j]<min:
                min=arr[j]
                index=j
            j+=1
        arr[pointer],arr[index]=arr[index],arr[pointer]
        pointer+=1
        self._selection(arr,pointer)
        return arr

def main():
    arr = [33, 15, 25, 12, 23, 17, 32, 22]
    sort = Sort(arr)

    print(sort.selection())

if __name__=="__main__":
    main()