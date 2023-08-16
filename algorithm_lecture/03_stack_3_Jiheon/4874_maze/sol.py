import sys
from collections import deque
sys.stdin = open('input.txt')

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def find_start(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return (i, j)

def bfs():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([find_start(maze)])
    while que:
        x, y = que.popleft()
        if maze[x][y] == 3:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and maze[nx][ny] != 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                que.append((nx, ny))
    return 0
        
T = int(input())
for t in range(T):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    print(f'#{t+1}', bfs())