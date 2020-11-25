# 팩토리얼 0의 개수
# 1676

# 문제
# N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

# 출력
# 첫째 줄에 구한 0의 개수를 출력한다.

# 입력 예제 1
# 10
# 3

# 출력 예제 1
# 2
# 0

import sys
f = sys.stdin
N = int(f.readline().strip())
if N <= 1:
    print(0)
else:
    numTwo = 0
    numFive = 0
    for i in range(1, N+1):
        num = i
        while(True):
            if num % 2 == 0:
                numTwo += 1
                num = num // 2
            else:
                break
        while(True):
            if num % 5 == 0:
                numFive += 1
                num = num // 5
            else:
                break
    print(min(numTwo, numFive))


