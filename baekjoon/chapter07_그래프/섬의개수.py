# 섬의 개수
# 4963

# 문제
# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다.
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다.
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

# 입력
# 입력은 여러 개의 테스트 케이스로 이루어져 있다.
# 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.
# 둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.
# 입력의 마지막 줄에는 0이 두 개 주어진다.

# 출력
# 각 테스트 케이스에 대해서, 섬의 개수를 출력한다.

# 입력 예제 1
# 1 1
# 0
# 2 2
# 0 1
# 1 0
# 3 2
# 1 1 1
# 1 1 1
# 5 4
# 1 0 1 0 0
# 1 0 0 0 0
# 1 0 1 0 1
# 1 0 0 1 0
# 5 4
# 1 1 1 0 1
# 1 0 1 0 1
# 1 0 1 0 1
# 1 0 1 1 1
# 5 5
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0 0 0 0
# 1 0 1 0 1
# 0 0

# 출력 예제 1
# 0
# 1
# 1
# 3
# 1
# 9
import sys
f = sys.stdin
dx = [1,-1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]
def dfs(x, y):
    from collections import deque
    d = deque()
    d.append([x, y])
    check[x][y] = 1
    
    while(len(d) != 0):
        x, y = d.pop()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < H and ny >= 0 and ny < W:
                if island[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    d.append([nx, ny])


while(True):
    W, H = map(int, f.readline().strip().split(" "))# w: 가로, h : 세로
    if W == 0 and H == 0:
        break
    else:
        island = [list(map(int, f.readline().strip().split(" "))) for _ in range(H)]
        check = [[0 for _ in range(W)] for _ in range(H)]
        cnt = 0
        for i in range(H):
            for j in range(W):
                if island[i][j] == 1 and check[i][j] == 0:
                    cnt += 1
                    dfs(i, j)
        print(cnt)


