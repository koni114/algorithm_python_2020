# 팩토리얼
# 1872

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# 입력 예제
# 10

# 출력 예제
# 3628800

import sys
f = sys.stdin
N = int(f.readline().strip())
def factorial(N):
    if N <= 1: return 1
    else:
        return N * factorial(N-1)
print(factorial(N))




