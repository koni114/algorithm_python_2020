# 순열사이클
# 10451

# 문제
# https://www.acmicpc.net/problem/10451

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스의 첫째 줄에는 순열의 크기 N (2 ≤ N ≤ 1,000)이 주어진다.
# 둘째 줄에는 순열이 주어지며, 각 정수는 공백으로 구분되어 있다.

# 출력
# 각 테스트 케이스마다, 입력으로 주어진 순열에 존재하는 순열 사이클의 개수를 출력한다.

# 입력 예제 1
# 2
# 8
# 3 2 7 8 1 4 5 6
# 10
# 2 1 3 4 5 6 7 9 10 8

# 출력 예제 1
# 3
# 7

import sys
f = sys.stdin
N = int(f.readline().strip())
for _ in range(N):
    P = int(f.readline().strip())
    check = [0 for i in range(P+1)]
    arr = list(map(int, f.readline().strip().split(" ")))
    cnt = 0
    for i in range(1, len(check)):
        if not check[i]:
            tmp = i
            check[tmp] = 1
            while(True):
                if check[arr[tmp-1]]:
                    cnt += 1
                    break
                else:
                    tmp = arr[tmp - 1]
                    check[tmp] = 1
    print(cnt)







