# 국영수
# 10825

# 문제
# 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다.
# 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 도현이네 반의 학생의 수 N (1 ≤ N ≤ 100,000)이 주어진다.
# 둘째 줄부터 한 줄에 하나씩 각 학생의 이름, 국어, 영어, 수학 점수가 공백으로 구분해 주어진다.
# 점수는 1보다 크거나 같고,
# 100보다 작거나 같은 자연수이다.
# 이름은 알파벳 대소문자로 이루어진 문자열이고, 길이는 10자리를 넘지 않는다.

# 출력
# 문제에 나와있는 정렬 기준으로 정렬한 후 첫째 줄부터 N개의 줄에 걸쳐 각 학생의 이름을 출력한다.

# 예제 입력 1
# 12
# Junkyu 50 60 100
# Sangkeun 80 60 50
# Sunyoung 80 70 100
# Soong 50 60 90
# Haebin 50 60 100
# Kangsoo 60 80 100
# Donghyuk 80 60 100
# Sei 70 70 70
# Wonseob 70 70 90
# Sanghyun 70 70 80
# nsj 80 80 80
# Taewhan 50 60 90

# 예제 출력 1
# Donghyuk
# Sangkeun
# Sunyoung
# nsj
# Wonseob
# Sanghyun
# Sei
# Kangsoo
# Haebin
# Junkyu
# Soong
# Taewhan

# 출력 예제 1
import sys
from collections import deque
dq = deque()
f = sys.stdin
N = int(f.readline().strip())
for i in range(N):
    a, b, c, d = f.readline().strip().split(" ")
    dq.append([a, int(b), int(c), int(d)])
dq = list(dq)
dq.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))
for i in dq:
    a, b, c, d = i
    print(a)