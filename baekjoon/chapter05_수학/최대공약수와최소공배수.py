# 최대공약수와 최대공배수
# 2609

# 문제
# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에는 두 개의 자연수가 주어진다. 이 둘은 10,000이하의 자연수이며 사이에 한 칸의 공백이 주어진다.

# 출력
# 첫째 줄에는 입력으로 주어진 두 수의 최대공약수를, 둘째 줄에는 입력으로 주어진 두 수의 최소 공배수를 출력한다.

# 예제 입력1
# 24 18

# 예제 출력1
# 6
# 72

import sys
f = sys.stdin
A, B = map(int, f.readline().strip().split())

def GCD(A, B):
    if B == 0:
        return A
    else:
        return GCD(B, A%B)

k = GCD(A, B)
print(k)
print(k * (A // k) * (B // k))
