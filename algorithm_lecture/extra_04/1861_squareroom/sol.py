import sys
sys.stdin = open('input.txt')

delta = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(start):
    cnt = 0
    stack = [start]
    while stack:
        x, y = stack.pop()
        cnt += 1
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < N and rooms[x][y] + 1 == rooms[nx][ny]:
                stack.append((nx, ny))
    return cnt

T = int(input())
for t in range(T):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    rlt = [float('inf'), 0]

    for i in range(N):
        for j in range(N):
            cnt = dfs((i, j))
            if cnt > rlt[1]:
                rlt[1] = cnt
                rlt[0] = rooms[i][j]
            elif cnt == rlt[1]:
                rlt[0] = min(rooms[i][j], rlt[0])
    print(f'#{t+1}', *rlt)