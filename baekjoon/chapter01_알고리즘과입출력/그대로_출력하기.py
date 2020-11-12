# 문제 : 입력 받은 대로 출력하는 프로그램을 작성하시오.
# 입력 : 입력이 주어진다. 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다.
#       각 줄은 100글자를 넘지 않으며, 빈 줄은 주어지지 않는다. 또, 각 줄은 공백으로 시작하지 않고, 공백으로 끝나지 않는다.

# 출력 : 입력받은 그대로 출력한다.
# 예제 입력
# Hello
# Baekjoon
# Online Judge

# 예제 출력
# Hello
# Baekjoon
# Online Judge

## error
# sys.stdin.readline()은 맨 끝의 개행문자까지 저장
# 이걸 그대로 print에 넣으면 그 개행문자를 출력한 다음 한 번 더 개행하기 때문에 줄 사이사이에 빈 줄이 들어가게 됩니다.
import sys
inf = sys.stdin
while(True):
    f = inf.readline()
    if(len(f) != 0): print(f)
    else: break
    
# 정답 코드.
# input code는 EOFError를 발생시킴
import sys

while True:
    line = input()
    if not line: break
    print(line)

while(True):
    try:
        print(input())
    except EOFError:
        break

