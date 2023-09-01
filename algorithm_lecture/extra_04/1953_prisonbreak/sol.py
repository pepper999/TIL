import sys
sys.stdin = open('input.txt')

from collections import deque

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
pipe = [[], [0, 1, 2, 3], [1, 3], [0, 2], [1, 2], [3, 2], [3, 0], [1, 0]]

def dfs(x, y):
    que = [[x, y]]
    visited[x][y] = 1
    while que:
        nowx, nowy = que.pop()
        able = pipe[tunnel[nowx][nowy]]
        for i in able:
            nx = nowx + delta[i][0]
            ny = nowy + delta[i][1]
            if 0 <= nx < N and 0 <= ny < M and tunnel[nx][ny]:
                if not visited[nx][ny] or visited[nx][ny] > visited[nowx][nowy] + 1:
                    next = pipe[tunnel[nx][ny]]
                    for j in next:
                        mx, my = nx + delta[j][0], ny + delta[j][1]
                        if mx == nowx and my == nowy:
                            visited[nx][ny] = 1 + visited[nowx][nowy]
                            que.append([nx, ny])

T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    dfs(R, C)
    rlt = 0
    for i in range(N):
        for j in range(M):
            if 0 < visited[i][j] <= L:
                rlt += 1
    print(f'#{t+1}', rlt)