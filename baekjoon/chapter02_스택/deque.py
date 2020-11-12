# deque function 기능.

from collections import deque
d = deque([1,2,3])
print(d)


# 1. deque.append
# 배열의 오른쪽에서 append
d.append(4)
print(d)

# 2. deque.appendleft
# 배열의 왼쪽에서 append
d.appendleft(10)
print(d)

# 3. deque.pop
# 배열의 오른쪽에서 pop
number = d.pop()
print(d)

# 4. deque.popleft
# 배열의 왼쪽에서 pop
number = d.popleft()
print(d)

# 5. deque.rotate
# 요소들을 입력 숫자 만큼 rotate 시켜주는 함수
d= deque([1,2,3,4,5])

# 양수 입력시, 오른쪽으로 회전
d.rotate(2)
print(d)

# 음수 입력시, 왼쪽으로 회전
d.rotate(-2)
print(d)
