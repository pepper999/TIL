import sys
sys.stdin = open('input.txt')

def search(x, y):
    startx, starty = x, y
    while 0 <= x < N and warehouse[x][y]:
       x += 1
    x -= 1
    while 0 <= y < N and warehouse[x][y]:
        y += 1
    y -= 1
    for i in range(startx, x+1):
        for j in range(starty, y+1):
            visited[i][j] = 1
    return x - startx + 1, y - starty + 1



T = int(input())
for t in range(T):
    N = int(input())
    warehouse = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    rlt = []
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and warehouse[i][j]:
                rlt.append(search(i,j))
    rlt.sort(key = lambda rlt: (rlt[0] * rlt[1], rlt[0]))
    print(f'#{t+1}', len(rlt), end = ' ')
    for i in range(len(rlt)):
        print(*rlt[i], end = ' ')
    print()