# 문제 : 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
#       각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 출력 : 각 테스트 케이스마다 A+B를 출력한다.
# 예제 입력
# 5
# 1 1
# 2 3
# 3 4
# 9 8
# 5 2

# 예제 출력
# 2
# 5
# 7
# 17
# 7
## 답안1
import sys
inf = sys.stdin
n = int(inf.readline())
number = 0
for i in range(n):
    int_std = inf.readline().split()
    number = 0
    for j in int_std:
        number += int(j)
    print(number)

## 답안2
import sys
inf = sys.stdin
testCases = int(inf.readline())

for _ in range(testCases):
    tmp = [int(i) for i in inf.readline().split()]
    print(sum(tmp))



