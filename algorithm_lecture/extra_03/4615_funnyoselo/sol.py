import sys
sys.stdin = open('input.txt')

delta = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def is_change(x, y, delta):
    k = 1
    nx = x + delta[0] * k
    ny = y + delta[1] * k
    while 0 <= nx < N and 0 <= ny < N:
        if board[nx][ny] == board[x][y]:
            return 1
        elif board[nx][ny] == 0:
            return 0
        k += 1
        nx = x + delta[0] * k
        ny = y + delta[1] * k
    return 0

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    board = [[0 for _ in range(N)] for _ in range(N)]
    mid = N // 2
    board[mid][mid] = -1
    board[mid-1][mid-1] = -1
    board[mid-1][mid] = 1
    board[mid][mid - 1] = 1
    for _ in range(M):
        x, y, color = map(int, input().split())
        x -= 1
        y -= 1
        if color == 1:
            board[x][y] = 1
        else:
            board[x][y] = -1
        for i in range(8):
            if is_change(x, y, delta[i]):
                k = 1
                nx = x + delta[i][0] * k
                ny = y + delta[i][1] * k
                while board[nx][ny] != board[x][y]:
                    board[nx][ny] *= -1
                    k += 1
                    nx = x + delta[i][0] * k
                    ny = y + delta[i][1] * k
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                cnt1 += 1
            elif board[i][j] == -1:
                cnt2 += 1
    print(f'#{t+1}', cnt1, cnt2)
