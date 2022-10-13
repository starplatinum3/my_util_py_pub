# from cmath import pi


def partition(arr,low,high): 
    i = ( low-1 )         # 最小元素索引
    pivot = arr[high]     
  
    for j in range(low , high): 
        # print("arr",arr)
        # print("如果arr[j] <= pivot，会swap arr[i]和arr[j]")
        # 当前元素小于或等于 pivot 
        print("j",j)
        if   arr[j] <= pivot: 
            print("pivot",pivot)
            # printListHighlighted(arr,[j])
          
            i = i+1 
            print("swap arr[i]和arr[j],找到右边的比基准小的 放到左边去")
            printListHighlighted(arr,[i,j])
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
def printListHighlighted(arr,highlightedIndexes):
    len_arr=len(arr)
    for i in range(len_arr):
        val=arr[i]
        if i in highlightedIndexes:
            print(f"({val})",end=" ")
        else:
            print(f"{val}",end=" ")
    print()
 
# arr[] --> 排序数组
# low  --> 起始索引
# high  --> 结束索引
  
# 快速排序函数
def quickSort(arr,low,high): 
    if low < high: 
  
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
  
# arr = [10, 7, 8, 9, 1, 5] 
arr = [10, 7, 8, 9, 1, 5,4] 
n = len(arr) 
quickSort(arr,0,n-1) 
print ("排序后的数组:") 
# for i in range(n): 
#     print ("%d" %arr[i]),
print(arr)
#     排序后的数组:
# 1
# 5
# 7
# 8
# 9
# 10