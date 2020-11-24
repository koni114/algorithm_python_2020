# 소수 구하기
# 1929

# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000) M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

# 예제 입력 1
# 3 16

# 예제 출력 1
# 3
# 5
# 7
# 11
# 13

import sys
f = sys.stdin
a,b = map(int, f.readline().strip().split(" "))
AT = [True for _ in range(b+1)]
AT[0] = False
AT[1] = False
for i in range(2, b+1):
    if i*i > b: break
    if AT[i]:
        for j in range(i*2, b+1, i):
            AT[j] = False

for i in range(a, b+1):
    if AT[i]:
        print(i)


