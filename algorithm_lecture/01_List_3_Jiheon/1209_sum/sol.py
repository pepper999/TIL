import sys
sys.stdin = open('input.txt')

# 100 x 100 행렬이기 때문에, 모든 경우를 다 프린트하는 식으로 진행
for t in range(10):
    number = int(input())
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))
    # 각 row의 합을 도출하여, max 값을 찾는 작업
    row_max = 0
    for i in range(100):
        if sum(matrix[i]) > row_max:
            row_max = sum(matrix[i])
    # 각 col의 합을 도출하여, max 값을 찾는 작업
    col_max = 0            
    for i in range(100):
        temp_sum = 0
        for j in range(100):
            temp_sum += matrix[j][i]
        if temp_sum > col_max:
            col_max = temp_sum
    # diagonal 원소의 합을 도출
    temp_sum = 0
    diagonal_max = 0
    for i in range(100):
        diagonal_max += matrix[i][i]
    # reverse diagonal 원소의 합을 도출
    r_diagonal_max = 0
    for i in range(100):
        r_diagonal_max += matrix[i][-i-1]

    print(f'#{number}', max(row_max, col_max, diagonal_max, r_diagonal_max))