# 문제
# 요세푸스 문제는 다음과 같다.
# 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고,
# 양의 정수 K(≤ N)가 주어진다.
# 이제 순서대로 K번째 사람을 제거한다.
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다.
# 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다.
# 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다.
# 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
# N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

# 출력
# 예제와 같이 요세푸스 순열을 출력한다.

# 예제 입력
# 7 3

# 예제 출력
# <3, 6, 2, 7, 5, 1, 4>
# 정답1
import sys
from collections import deque
f = sys.stdin
N, K = map(int, f.readline().strip().split(" "))
d = deque(range(1, N+1))
final = deque()

while(True):
    if len(d) == 0:
        break
    for _ in range(K-1):
        d.append(d.popleft())
    final.append(str(d.popleft()))
print("<" + str(", ".join(final)) + ">")

# 정답2 더 빠름
from collections import deque
import sys
f = sys.stdin
N, M = [int(i) for i in f.readline().split()]
N_list = deque(range(1, N+1))
i = 0
print("<", end = "")
while(len(N_list) != 0):
    N_list.rotate(-(M - 1))
    if i != len(N_list)-1:
        print(N_list.popleft(), end = ", ")
    else:
        print(N_list.popleft(), end="")
print(">", end = "")


