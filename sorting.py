from ll import ll
class Sort:
    def __init__(self,data):
        self.arr=data

    def selection(self):
        arr=self.arr
        for i in range(len(arr)):
            min=arr[i]
            index=i

            for j in range(i+1,len(arr)):
                if arr[j]<min:
                    index=j
                    min=self.arr[j]

            arr[i],arr[index]=arr[index],arr[i]

        return arr

    def insersion(self):
        for i in range(1,len(self.arr)):
            key=self.arr[i]
            j=i-1
            while j>=0 and key<self.arr[j]:
                self.arr[j+1]=self.arr[j]
                j-=1

            self.arr[j+1]=key

        return self.arr

    def bubble(self):
        for i in range(len(self.arr)):
            for j in range(1,len(self.arr)):
                if self.arr[j]<self.arr[j-1]:
                    self.arr[j - 1],self.arr[j]=self.arr[j],self.arr[j - 1]

        return self.arr

    def qucik(self):
        return self._quicksort_recursion(self.arr)

    def _quicksort_recursion(self,arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        i = -1
        for j in range(len(arr)):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[j] = arr[j], arr[i + 1]
        left_partition = self._quicksort_recursion(arr[:i + 1])
        right_partition = self._quicksort_recursion(arr[i + 2:])
        return left_partition + [arr[i + 1]] + right_partition

    def merge(self):
        return self._merge_sort_recursion(self.arr)

    def _merge_sort_recursion(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_arr = self._merge_sort_recursion(arr[:mid])
        right_arr = self._merge_sort_recursion(arr[mid:])
        return self._merge(left_arr, right_arr, arr)

    def _merge(self, left_arr, right_arr, arr):
        left, right = len(left_arr), len(right_arr)
        l, r, i = 0, 0, 0
        while l < left and r < right:
            if left_arr[l] < right_arr[r]:
                arr[i] = left_arr[l]
                l += 1
            else:
                arr[i] = right_arr[r]
                r += 1
            i += 1
        while l < left:
            arr[i] = left_arr[l]
            i += 1
            l += 1
        while r < right:
            arr[i] = right_arr[r]
            i += 1
            r += 1
        return arr

    def bucket(self):
        bucket=[ll() for _ in range(max(self.arr)+1)]
        output=[]

        for i in self.arr:
            bucket[i].add_node(i)

        for i in range(len(bucket)):
            length=bucket[i].length

            while length>=0:
                item = bucket[i].del_node_begin()
                if item is not None:
                    output.append(item)
                length-=1

        return output

    def radixsort(self):
        max_value=max(self.arr)
        count = 0 # For counting maximum digit of a number in an array
        arr=self.arr.copy()

        while max_value > 0:
            count += 1
            max_value = max_value // 10

        for i in range(count):
            arr=self._radix_helper(arr,i)
        return arr

    def _radix_helper(self,arr,position):
        bucket = [ll() for _ in range(max(arr) + 1)]
        output = []
        digit_arr=arr.copy()

        while position>0:
            for i in range(len(digit_arr)):
                digit_arr[i]=digit_arr[i]//10
            position-=1

        for i in range(len(arr)):
            bucket[digit_arr[i]%10].add_node(arr[i])

        for i in range(len(bucket)):
            length = bucket[i].length

            while length >= 0:
                item = bucket[i].del_node_begin()
                if item is not None:
                    output.append(item)
                length -= 1
        return output

def main():
    arr=[33,15,25,12,23,17,32,22]
    sort=Sort(arr)

    print(sort.selection())


if __name__=="__main__":
    main()