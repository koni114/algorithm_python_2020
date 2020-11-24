# 소인수분해
# 11653

# 문제
# 정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

# 출력
# N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다.

# 입력 예제
# 72

# 출력 예제
# 2
# 2
# 2
# 3
# 3

import sys
import math
from collections import  deque
d = deque()
f = sys.stdin
N = int(f.readline().strip())
if N == 1: print("")
else:
    for i in range(2, round(math.sqrt(N)) + 1):
        if N == 1: break
        while(True):
            if not N % i == 0:
                break
            else:
                d.append(i)
                N = N // i

    if not N == 1: d.append(N)

    if len(d) == 0:
        print(N)
    else:
        for i in range(len(d)):
            print(d[i])
