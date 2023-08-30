import sys
sys.stdin = open('input.txt')

def dfs():
    delta = [(0, 1), (1, 0)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    stack = [[0,0]]
    visited[0][0] = box[0][0]
    while stack:
        x, y = stack.pop()
        for i in range(2):
            nx = x + delta[i][0]
            ny = y + delta[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] or visited[nx][ny] > visited[x][y] + box[nx][ny]:
                    visited[nx][ny] = visited[x][y] + box[nx][ny]
                    stack.append([nx, ny])
    return visited

T = int(input())
for t in range(T):
    N = int(input())
    box = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t+1}', dfs())