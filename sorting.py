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

            arr[i]=arr[index]
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

    def quciksort(self):
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

    def mergesort(self):
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

    def bucket_sort(self):
        length=len(self.arr)
        max_val=max(self.arr)
        min_val = min(self.arr)
        range_val=max_val-min_val+1

        buckets=[[] for _ in range(length)]

        for i in self.arr:
            index=(min_val * i) * (max_val-1)//range_val
            buckets[index].append(i)
        self.arr.clear()
        for bucket in buckets:
            self.arr.extend(sorted(bucket))
        return self.arr

    def radix_sort(self):
        pass

def main():
    arr=[8,2,4,7,1,3,9,6,5]
    sort=Sort(arr)

    print(sort.bucket_sort())

if __name__=="__main__":
    main()