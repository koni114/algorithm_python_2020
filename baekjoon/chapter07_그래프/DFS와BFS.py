# DFS와 BFS
# 1260

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다.
# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

# 입력 예제 1
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

# 1000 1 1000
# 999 1000

# 출력 예제 1
# 1 2 4 3
# 1 2 3 4

# 3 1 2 5 4
# 3 1 4 2 5

# 1000 999
# 1000 999

import sys
from collections import deque
d = deque()
dfsArr = deque()
bfsArr = deque()
f = sys.stdin
nodeNum, edgeNum, startNode = map(int, f.readline().strip().split(" "))
arr = [deque() for _ in range(nodeNum+1)]
check = [0 for _ in range(nodeNum+1)]
for i in range(edgeNum):
    a, b = map(int, f.readline().strip().split(" "))
    arr[a].append(b)
    arr[b].append(a)
arr = [sorted(x) for x in arr]

def dfs(x):
    check[x] = 1
    dfsArr.append(str(x))
    for i in range(len(arr[x])):
        y = arr[x][i]
        if check[y] == 0:
            dfs(y)

def bfs(x):
    queue = deque()
    check[x] = 1
    queue.append(x)
    while(len(queue) != 0):
        tmp = queue.popleft()
        bfsArr.append(str(tmp))
        for i in range(len(arr[tmp])):
            y = arr[tmp][i]
            if check[y] == 0:
                check[y] = 1
                queue.append(y)

dfs(startNode)
check = [0 for _ in range(nodeNum+1)]
bfs(startNode)
print(" ".join(dfsArr))
print(" ".join(bfsArr))





