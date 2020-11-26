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

## 파이썬 정렬 함수
# 1차원 배열 정렬
test = [5,1,4,3,2]
test.sort()                #- 오름차순 정렬
test.sort(reverse = True)  #- 내림차순 정렬

# 2차원 배열 정렬
test = [
    [1, 1],
    [5, 3],
    [2, 2],
    [2, 3],
    [5, 3]
]
sorted(test, key=lambda x: x[1])
# 아이템 첫 번째 인자를 기준으로 오름차순으로 먼저 정렬하고,
# 그리고 그 안에서 다음 두 번째 인자를 기준으로 내림차순으로 정렬하게 하려면, 다음과 같이 할 수 있다.
sorted(test, key=lambda x: (x[0], -x[1]))
