# 미로 탐색
# 2178

# N×M크기의 배열로 표현되는 미로가 있다.
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여
# (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

# 입력
# 첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다.
# 각각의 수들은 붙어서 입력으로 주어진다.

# 출력
# 첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.

# 입력 예제 1
# 4 6
# 101111
# 101010
# 101011
# 111011

# 4 6
# 110110
# 110110
# 111111
# 111101

# 2 25
# 1011101110111011101110111
# 1110111011101110111011101

# 7 7
# 1011111
# 1110001
# 1000001
# 1000001
# 1000001
# 1000001
# 1111111

# 출력 예제 1
# 15
# 9
# 38
# 13
import sys
f = sys.stdin
N, M = map(int, f.readline().strip().split(" "))
maze = [[int(i) for i in list(f.readline().strip())] for _ in range(N)]
check = [[0 for _ in range(M)] for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    from collections import deque
    d = deque()
    cnt = 1
    d.append([x, y, cnt])
    check[x][y] = 1
    while(len(d) != 0):
        x, y, c = d.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if maze[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = c+1
                    d.appendleft([nx, ny, c+1])

    return check[N-1][M-1]
print(bfs(0,0))


