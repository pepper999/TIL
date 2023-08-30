import sys
sys.stdin = open('input.txt')
from collections import deque

delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs():
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny])

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    que = deque([])
    for i in range(N):
        maps = list(input())
        for j in range(M):
            if maps[j] == 'W':
                visited[i][j] = 0
                que.append([i, j])
    bfs()
    total = 0
    for i in range(N):
        for j in range(M):
            total += visited[i][j]
    print(f'#{t+1}', total)