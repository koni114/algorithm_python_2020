# 가장 큰 증가하는 부분 수열
# 11055

# 문제
# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 합이 가장 큰 증가 부분 수열의 합을 출력한다.

# 입력 예제 1
# 10
# 1 100 2 50 60 3 5 6 7 8

# 출력 예제 1
# 113
import sys
f = sys.stdin
N = int(f.readline().strip())
arr = list(map(int, f.readline().strip().split(" ")))
dp = [0 for _ in range(N)]

if N == 1:
    print(arr[0])
else:
    for i in range(N):
        tmp = arr[i]
        for j in range(0, i):
            if arr[i] > arr[j]:
                tmp = max(tmp, dp[j] + arr[i])
        dp[i] = tmp
    print(max(dp))







