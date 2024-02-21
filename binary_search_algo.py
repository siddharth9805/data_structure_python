class binary_search:
    def __init__(self,arr):
        self.array_data=arr
    def find(self,value)->bool:
        return self._search(self.array_data,0,len(self.array_data)-1,value)
    def _search(self,arr,start,end,value)->bool:
        mid=(start+end)//2

        if arr[mid] == value:
            return True
        elif mid==0 or mid==end:
            return False
        elif value<arr[mid]:
            return self._search(arr,0,mid-1,value)
        elif value>arr[mid]:
            return self._search(arr,mid+1,end,value)

def main():
    arr=[1,2,3,4]
    obj=binary_search(arr)
    k=obj.find(-1)
    print(k)

if __name__=="__main__":
    main()