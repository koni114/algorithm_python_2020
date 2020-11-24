# -2진수
# 2089

# 문제
# -2진법은 부호 없는 2진수로 표현이 된다.
# 2진법에서는 20, 21, 22, 23이 표현 되지만 -2진법에서는 (-2)0 = 1, (-2)1 = -2, (-2)2 = 4, (-2)3 = -8을 표현한다.
# 10진수로 1부터 표현하자면 1, 110, 111, 100, 101, 11010, 11011, 11000, 11001 등이다.
# 10진법의 수를 입력 받아서 -2진수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 10진법으로 표현된 수 N(-2,000,000,000≤N≤2,000,000,000)이 주어진다.

# 출력
# -2진법 수를 출력한다.

# 예제 입력
# -13

# 예제 출력
# 110111
import sys
from collections import deque
d = deque()
f = sys.stdin
N = int(f.readline().strip())
if N == 0: print(0)
else:
    while(True):
        if abs(N) <= 1:
            if N == -1:
                d.extendleft([1,1])
            elif N == 1:
                d.appendleft(1)
            break
        a, b = divmod(N, -2)
        if b == 0:
            d.appendleft(b)
            N = a
        else:
            d.appendleft(b+2)
            N = a+1

    for i in range(len(d)):
        if i == len(d)-1:
            print(str(d[i]))
        else:
            print(str(d[i]), end = "")