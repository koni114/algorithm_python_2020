# 좌표 정렬하기 2

# 문제
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다. (-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

# 출력
# 첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.

# 입력 예제 1
# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3

# 출력 예제 1
# 1 -1
# 1 2
# 2 2
# 3 3
# 0 4
import sys
from collections import deque
d = deque()
f = sys.stdin
N = int(f.readline().strip())
for i in range(N):
    d.append(list(map(int, f.readline().strip().split(" "))))
d = list(d)
d.sort(key = lambda x: (x[1], x[0]))
for i in range(N):
    a, b = d[i]
    print(a, b)

