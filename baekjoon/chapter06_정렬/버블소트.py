# 버블소트
# 1377

# 문제
# 영식이는 다음과 같은 버블 소트 프로그램을 C++로 작성했다.
# https://www.acmicpc.net/problem/1377
# 위 소스에서 n은 배열의 크기이고, a는 수가 들어있는 배열이다. 수는 배열의 1번방부터 채운다.
# 위와 같은 소스를 실행시켰을 때, 어떤 값이 출력되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다.
# N은 500,000보다 작거나 같은 자연수이다.
# 둘째 줄부터 N개의 줄에 A[1]부터 A[N]까지 하나씩 주어진다.
# A에 들어있는 수는 1,000,000보다 작거나 같은 자연수 또는 0이다.

# 출력
# 정답을 출력한다.

# 입력 예제 1
# 5
# 10
# 1
# 5
# 2
# 3

# 출력 예제 1
# 3

# 답안 1
import sys
from collections import deque
d = deque()
f = sys.stdin
N = int(f.readline().strip())
num = 0
for i in range(N):
    d.append([int(f.readline().strip()), i])
d = sorted(list(d), key = lambda x : (x[0], x[1]))

for i in range(len(d)):
    num = max(num, d[i][1] - i)
print(num+1)

# 답안 2 --> enumerate 사용
import sys
from collections import deque
d = deque()





