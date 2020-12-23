# split
items = "zero one two three".split()
print(items)

items = "zero,one,two, three".split(",")
print(items)

colors = ['red', 'blue', 'green', 'yellow']
", ".join(colors)

# List comprehension
# --> 일반적으로 for + append 보다 성능이 좋음
results = [i for i in range(10)]
print(results)

word_1 = 'hello'
word_2 = 'world'
[i+j for i in word_1 for j in word_2]
[[i+j for i in word_1] for j in word_2]

word_1 = ["A", "B", "C"]
word_2 = ["B", "C", "A"]
[i+j for i in word_1 for j in word_2 if (i == j)]

words = 'The quick brown fox jumps over the lazy dog'.split()
[[i.upper(), i.lower(), len(i)] for i in words]

for i, j in enumerate(['tic', 'tac', 'toc']):
    print(i, j)

{i:j for i,j in enumerate('good day to die'.split())}

## zip
## 두 리스트의 값을 병렬적으로 추출 함
list1 = [1,2,3]
list2 = [4,5,6]
for i,j in zip(list1, list2):
    print(i, j)

a, b, c = zip((1,2,3), (10, 20, 30), (100, 200, 300))

a = [1,2,3]
b = [10, 20, 30]
c = [100, 200, 300]
[sum(x) for x in zip(a,b,c)]

# 8진법 --> 10진법으로 변경 방법.
int("100", 8)

def bubbleSort(arr):
    for i in range(len(arr)):
        check = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                check = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not check:
            break
    return arr


bubbleSort([1,2,3,4,5])

from os import getcwd
getcwd()