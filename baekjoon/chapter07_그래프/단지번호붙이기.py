# 단지 번호 붙이기
# 2667

# 문제
# https://www.acmicpc.net/problem/2667

# 입력
# 첫 번째 줄에는 지도의 크기 N(정사각형이므로 가로와 세로의 크기는 같으며 5≤N≤25)이 입력되고,
# 그 다음 N줄에는 각각 N개의 자료(0혹은 1)가 입력된다.

# 출력
# 첫 번째 줄에는 총 단지수를 출력하시오.
# 그리고 각 단지내 집의 수를 오름차순으로 정렬하여 한 줄에 하나씩 출력하시오.

# 입력 예제
# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000

# 출력 예제
# 3
# 7
# 8
# 9

import sys
from collections import deque
f = sys.stdin
N = int(f.readline().strip())
arr = [[int(i) for i in list(f.readline().strip())] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
check = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
houseNum = deque()

def bfs(x, y):
    from collections import deque
    d = deque()
    d.append([x, y])
    check[x][y] = 1
    houseCnt = 1

    while(len(d) != 0):
        x, y = d.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if  nx >= 0 and nx < N and ny >= 0 and ny < N:
                if arr[nx][ny] == 1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    houseCnt += 1
                    d.append([nx, ny])
    return houseCnt

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and check[i][j] == 0:
            cnt += 1
            houseNum.append(bfs(i, j))

print(cnt)
houseNum = sorted(houseNum)
for i in range(cnt):
    print(houseNum[i])





