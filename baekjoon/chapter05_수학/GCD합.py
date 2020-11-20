# GCD합
# 양의 정수 n개가 주어졌을 때, 가능한 모든 쌍의 GCD의 합을 구하는 프로그램을 작성하시오.

# 첫째 줄에 테스트 케이스의 개수 t (1 ≤ t ≤ 100)이 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있다.
# 각 테스트 케이스는 수의 개수 n (1 < n ≤ 100)가 주어지고, 다음에는 n개의 수가 주어진다. 입력으로 주어지는 수는 1,000,000을 넘지 않는다.

# 각 테스트 케이스마다 가능한 모든 쌍의 GCD의 합을 출력한다.

# 예제 입력 1
# 3
# 4 10 20 30 40
# 3 7 5 12
# 3 125 15 25

# 예제 출력 1
# 70
# 3
# 35

import sys
f = sys.stdin
T = int(f.readline().strip())
def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A%B)


for _ in range(T):
    L = list(map(int, f.readline().strip().split()))
    num = 0
    for i in range(1, L[0]):
        for j in range(i+1, L[0]+1):
            num += GCD(L[i], L[j])
    print(num)





