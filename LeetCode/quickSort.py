class QuickSort:
    def __init__(self) -> None:
        pass
    def quickSort(low,high,arr):
        # for i in range()
        par=arr[low]
        while low<high:
            while low<high and arr[high]>=par:
                high-=1
            arr[low]=arr[high]
            while low<high and arr[low]<=par:
                low+=1
            arr[high]=arr[low]
        pass