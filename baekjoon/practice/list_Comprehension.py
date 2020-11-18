## 1. row 내의 element 접근하기
# 여기서 element 는 원소를 의미

# 2개 괄호 제거하기
matrix = [[1,2,3], [4,5,6], [7,8,9]]
matrix_row = [row_element for row in matrix for row_element in row ]

# 3개 괄호 제거하기
matrix = [[[1,2,3], [4,5,6]], [['a', 'b', 'c']]]
matrix_row = [row_element for matrix_e in matrix for row in matrix_e for row_element in row]
print(matrix_row)

## 2. 리스트를 살리면서 element 접근하기
# 단일 리스트 제곱하기
vector = [1,2,3,4,5,6,7,8,9]
vector_pow = [row_element ** 2 for row_element in vector]

# 다중 리스트 만들기(리스트 안의 리스트 만들기)
# 내가 계산하고 싶은 식 + 저장하고 싶은 형태
matrix = [[1,2,3], [4,5,6], [7,8,9]]
squared_vector = [[row_element ** 2 for row_element in matrix_e] for matrix_e in matrix]
print(squared_vector)


