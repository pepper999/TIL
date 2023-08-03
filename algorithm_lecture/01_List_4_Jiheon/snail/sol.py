def snail(num):
    matrix = [[0]*num for i in range(num)]
    x , y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    i = 1
    while i < num**2:
        matrix[x][y] = i
        for j in range(4):
            try:
                while matrix[x+dx[j]][y+dy[j]] == 0 and i <= num**2:
                    x += dx[j]
                    y += dy[j]
                    matrix[x][y] = i+1
                    i += 1
            except IndexError:
                continue
    return matrix


T = int(input())
for t in range(T):
    N = int(input())
    if N == 1:
        snail_mat = [[1]]
    snail_mat = snail(N)

    print(f'#{t+1}')
    for i in range(N):
        print(*snail_mat[i])
