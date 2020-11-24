# 소수 찾기
# 1978

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 입력 예제 1
# 4
# 1 3 5 7

# 출력 예제 1
# 3

import sys
import math
f = sys.stdin
T = int(f.readline().strip())
num = list(map(int, f.readline().strip().split(" ")))
def prime(N):
    if N < 2: return False
    for i in range(2, round(math.sqrt(N))+1):
        if N % i == 0: return False
    return True
print(sum([prime(num[i]) for i in range(T)]))
