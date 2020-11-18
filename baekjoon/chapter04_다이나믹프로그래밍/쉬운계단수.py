# 쉬운계단수
# 10844

# 문제
# 45656이란 수를 보자.
# 이 수는 인접한 모든 자리수의 차이가 1이 난다. 이런 수를 계단 수라고 한다.
# 세준이는 수의 길이가 N인 계단 수가 몇 개 있는지 궁금해졌다.
# N이 주어질 때, 길이가 N인 계단 수가 총 몇 개 있는지 구하는 프로그램을 작성하시오. (0으로 시작하는 수는 없다.)

# 입력
# 첫째 줄에 N이 주어진다. N은 1보다 크거나 같고, 100보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 정답을 1,000,000,000으로 나눈 나머지를 출력한다.

# 예제 입력 1
# 1
# 2

# 예제 입력 2
# 9
# 17

# dp[i][j] = i로 시작하는 숫자의 j자리 수의 계단 수의 수

import sys
f = sys.stdin
N = int(f.readline().strip())
dp = [[0 for _ in range(N+1)] for _ in range(10)]
number = 0
if N == 1:
    print(9)
else:
    for i in range(10):
        dp[i][1] = 1

    for j in range(2, N+1):
        for i in range(10):
            if i >= 1 and i <= 8:
                dp[i][j] = dp[i-1][j-1] +dp[i+1][j-1]
            elif i == 0:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]

    for i in range(1, 10):
        number += dp[i][N]
    print(number % 1000000000)