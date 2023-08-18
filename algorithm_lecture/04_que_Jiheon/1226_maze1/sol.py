import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(startx, starty):
    que = deque([[startx, starty]])
    visited = [[0 for _ in range(16)] for _ in range(16)]
    while que:
        x, y = que.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visited[nx][ny] and not maze[nx][ny]:
                que.append([nx, ny])
            elif maze[nx][ny] == 3:
                return 1
    return 0

for _ in range(10):
    T = int(input())
    maze = [list(map(int, list(input()))) for _ in range(16)]
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                rlt = bfs(i, j)
    print(f'#{T}', rlt)