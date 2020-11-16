# 문제
# https://www.acmicpc.net/problem/10799

# 입력
# 한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

# 출력
# 잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.

# 예제 입력
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())

# 예제 출력
# 17
# 24

# 정답1.
import sys
from collections import deque
stack = deque()
f = sys.stdin
bar = list(f.readline().strip())
number = 0

for i in range(len(bar)):
    if bar[i] == '(':
        stack.append(i)
    else:
        if bar[i-1] == '(':
            stack.pop()
            number += len(stack)
        else:
            stack.pop()
            number += 1
print(number)

# 정답2
# 더 좋은 성능. deque가 아닌, 단순 계산을 톻해 개선 가능.
import sys
f = sys.stdin
bar = f.readline().strip()
stack = 0
count = 0
for i in range(len(bar)):
    if bar[i] == '(':
        stack += 1
    else:
        stack -= 1
        if bar[i-1] == "(":
            count += stack
        else:
            count += 1
print(count)

