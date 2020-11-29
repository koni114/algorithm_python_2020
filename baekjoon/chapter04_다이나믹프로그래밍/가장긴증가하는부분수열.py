# 가장 긴 증가하는 부분 수열
# 11053

# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.

# 예제 입력 1
# 6
# 10 20 10 30 20 50

# 예제 출력 1
# 4

import sys
f = sys.stdin
N = int(f.readline().strip())
arr = list(map(int, f.readline().strip().split(" ")))
dp = [0 for _ in range(N)]
if N == 1:
    print(1)
else:
    dp[0] = 1
    for i in range(N):
        tmp = 1
        tmpValue = arr[i]
        for j in range(0, i):
            if tmpValue > arr[j]:
                tmp = max(dp[j] + 1, tmp)
        dp[i] = tmp
    print(max(dp))




