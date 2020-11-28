# 카드
# 11652

# 준규는 숫자 카드 N장을 가지고 있다. 숫자 카드에는 정수가 하나 적혀있는데, 적혀있는 수는 -262보다 크거나 같고, 262보다 작거나 같다.
# 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오. 만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다

# 입력
# 첫째 줄에 준규가 가지고 있는 숫자 카드의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개 줄에는 숫자 카드에 적혀있는 정수가 주어진다.

# 출력
# 첫째 줄에 준규가 가장 많이 가지고 있는 정수를 출력한다.

# 예제 입력 1
# 5
# 1
# 2
# 1
# 2
# 1

# 예제 출력 1
# 6
# 1
# 2
# 1
# 2
# 1

## 1차 풀이 : 일반적인 방법
import sys
from collections import deque
f = sys.stdin
N = int(f.readline().strip())
d = deque()
for _ in range(N):
    d.append(int(f.readline().strip()))

if N == 1:
    print(d[0])
else:
    d = sorted(d, reverse = True)
    maxCnt = 1
    maxValue = d[0]
    currCnt = 1
    currValue = d[0]

    for i in range(1, len(d)):
        if d[i-1] == d[i]:
            currCnt += 1
        else:
            if maxCnt <= currCnt:
                maxValue = currValue
                maxCnt = currCnt
            currValue = d[i]
            currCnt = 1

    if maxCnt <= currCnt:
        maxValue = currValue
        maxCnt = currCnt
    print(maxValue)

## 2차 풀이 : defaultDict 이용한 방법
import sys
from collections import defaultdict
f = sys.stdin
N = int(f.readline().strip())
d = defaultdict(lambda : 0)
for _ in range(N):
    d[int(f.readline().strip())] += 1
print(sorted(list(d.items()), key = lambda x : (-x[1], x[0]))[0][0])