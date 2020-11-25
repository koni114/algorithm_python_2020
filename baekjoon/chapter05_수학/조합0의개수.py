# 조합 0의 개수

# 문제
# nCm의 끝자리 0의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 n, m (0 ≤ m ≤ n ≤ 2,000,000,000, n ≠ 0)이 들어온다.

# 출력
# 첫째 줄에 0의 개수를 출력한다.

# 예제 입력 1
# 25 12

# 예제 출력 1
# 2

import sys
import math
f = sys.stdin
a, b = map(int, f.readline().strip().split(" "))
b = a - b
resultFive = 0
resultTwo = 0
i = 1
def combi(N, powNum):
    result = 0
    i = 1
    while(True):
        if N < math.pow(powNum, i):
            break
        else:
            result += int(N // math.pow(powNum, i))
            i += 1
    return result

resultTwo = combi(a, 2) - combi(a-b, 2) - combi(b, 2)
resultFive = combi(a, 5) - combi(a-b, 5) - combi(b, 5)
print(min(resultTwo, resultFive))

