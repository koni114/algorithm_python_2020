# 2진수 8진수
#

# 문제
# 2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 2진수가 주어진다. 주어지는 수의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 주어진 수를 8진수로 변환하여 출력한다.

# 입력 예제 1
# 11001100

# 출력 예제 1
# 314


## 시간초과
import sys
from collections import deque
d = ""
f = sys.stdin
N = f.readline().strip()
num = int(N, 2)

while(True):
    if num < 8:
        d += str(num)
        break
    else:
        d += (str(num % 8))
        num = num // 8

print(d[::-1])

