T = int(input())

def back(num, num_sum):
    global num_min
    if num_sum > num_min:
        return
    if num == N:
        num_min = min(num_sum, num_min)
        return
    for i in range(len(matrix[num])):
        if i not in visited:
            visited.append(i)
            back(num + 1, num_sum + matrix[num][i])
            visited.pop()

for t in range(T):
    visited = []
    num_min = 10 ** 5
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    back(0, 0)
    print(f'#{t+1}', num_min)