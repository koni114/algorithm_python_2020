# 연결 요소의 개수
# 11724

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
# 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.

# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

# 입력 예제 1
# 6 5
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6

# 6 8
# 1 2
# 2 5
# 5 1
# 3 4
# 4 6
# 5 4
# 2 4
# 2 3

# 출력 예제 1
# 2
# 1
import sys
from collections import deque
f = sys.stdin
nodeNum, edgeNum = map(int, f.readline().strip().split(" "))
arr = [deque() for _ in range(nodeNum + 1)]
for i in range(edgeNum):
    a, b = map(int, f.readline().strip().split(" "))
    arr[a].append(b)
    arr[b].append(a)
cnt = 0
queue = deque()
check = [0 for _ in range(nodeNum + 1)]
for i in range(1, nodeNum + 1):
    if check[i] == 0:
        cnt += 1
        queue.append(i)
        while(len(queue) != 0):
            y = queue.popleft()
            for j in range(len(arr[y])):
                tmp = arr[y][j]
                if check[tmp] == 0:
                    check[tmp] = 1
                    queue.append(tmp)
print(cnt)






