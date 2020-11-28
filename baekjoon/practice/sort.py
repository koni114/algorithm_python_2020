# 정렬

# selection sort
def selectionSort(arr):
    for i in range(len(arr)-1):
        tmp, tmpIdx = arr[i], i
        for j in range(i+1, len(arr)):
            if arr[j] < tmp:
                tmp, tmpIdx = arr[j], j
        if not i == j:
            arr[tmpIdx], arr[i] = arr[i], tmp
    return arr
selectionSort([3,5,1,2,4])
selectionSort([2,2,1])

# bubble sort
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return(arr)
bubbleSort([3,5,1,2,4])
bubbleSort([2,2,1])

# 향상된 bubble sort
def bubbleSort(arr):
    for i in range(len(arr)):
        check = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                check = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not check: break
    return(arr)

bubbleSort([3,5,1,2,4])
bubbleSort([2,2,1])

def insertSort(arr):
    for i in range(2, len(arr)):
        tmp = arr[i]
        for j in range(i-1, -2, -1):
            if  arr[j] > tmp and j >= 0:
                arr[j+1] = arr[j]
            else:
                arr[j+1] = tmp
                break
    return arr
insertSort([3,5,1,2,4])
insertSort([2,2,1])







