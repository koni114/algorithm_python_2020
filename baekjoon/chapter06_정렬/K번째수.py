# k번째 수
# 11004

# 문제
# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N(1 ≤ N ≤ 5,000,000)과 K (1 ≤ K ≤ N)이 주어진다.
# 둘째에는 A1, A2, ..., AN이 주어진다. (-109 ≤ Ai ≤ 109)

# 출력
# A를 정렬했을 때, 앞에서부터 K번째 있는 수를 출력한다.

# 입력 예제 1
# 5 2
# 4 1 2 3 5

# 출력 예제 1
# 2

import sys
f = sys.stdin
N, K = map(int, f.readline().strip().split(" "))
print(sorted(list(map(int, f.readline().strip().split(" "))))[K-1])

