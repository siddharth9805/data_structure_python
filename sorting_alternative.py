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

    def insersion(self):
        return self._insersion(self.arr,1)

    def _insersion(self,arr,pointer):
        if pointer==len(arr):
            return

        key=arr[pointer]
        j=pointer-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1

        arr[j+1]=key
        pointer+=1
        self._insersion(arr,pointer)
        return arr

    def bubble(self):
        return self._bubble(self.arr,0)

    def _bubble(self,arr,pointer):
        j=pointer+1
        while pointer<len(arr):
            if arr[pointer]<arr[j]:
                arr[pointer],arr[j]=arr[j],arr[pointer]
        pointer+=1
        self._bubble(arr,pointer)
        return arr

    def quick_sort(self):
        stack=[(0,len(self.arr))]

        while stack:
            start,end=stack.pop()
            if start >= end:
                continue

            pivote=self.arr[end-1]
            i=-1
            for j in range(end):
                if self.arr[j]<pivote:
                    i+=1
                    self.arr[i],self.arr[j]=self.arr[j],self.arr[i]

            self.arr[i + 1], self.arr[j]= self.arr[j],self.arr[i+1]
            stack.append((start,i+1))
            stack.append(((i+2,end)))
        return self.arr
def main():
    arr = [33, 15, 25, 12, 23, 17, 32, 22]
    sort = Sort(arr)

    print(sort.quick_sort())

if __name__=="__main__":
    main()