import sys
sys.stdin = open('input.txt')

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(startx, starty):
    visited = [[0 for _ in range(N)]for _ in range(N)]
    que = deque([[startx, starty]])
    while que:
        x, y = que.popleft()
        if maze[x][y] == 3:
            return visited[x][y] - 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                que.append([nx, ny])
    return 0

T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                startx, starty = i, j
    print(f'#{t+1}', bfs(startx, starty))




    