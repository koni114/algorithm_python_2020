# 반복수열
# 2331

# 문제
# 다음과 같이 정의된 수열이 있다.
# D[1] = A
# D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합

# 예를 들어 A=57, P=2일 때, 수열 D는 {57, 74(=5^2+7^2=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …}이 된다.
# 그 뒤에는 앞서 나온 수들(57부터가 아니라 58부터)이 반복된다.

# 이와 같은 수열을 계속 구하다 보면 언젠가 이와 같은 반복수열이 된다.
# 이때, 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 구하는 프로그램을 작성하시오.
# 위의 예에서는 {57, 74, 65, 61}의 네 개의 수가 남게 된다.

# 입력
# 첫째 줄에 A(1 ≤ A ≤ 9999), P(1 ≤ P ≤ 5)가 주어진다.

# 출력
# 첫째 줄에 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 출력한다.
import sys
f = sys.stdin
A, P = map(int, f.readline().strip().split(" "))
d = dict()
d[A] = 1
count = 1
def calPow(A, P):
    import math
    return(sum([int(math.pow(int(i), P)) for i in list(str(A))]))
while(True):
    A = calPow(A, P)
    if not d.get(A, 0):
        count += 1
        d[A] = count
    else:
        checkNum = d.get(A)
        break
print(checkNum-1)


