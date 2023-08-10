import sys
sys.stdin = open('input.txt')

def bfs(N, start):
    visited = [0]*(N+1)
    queue = [[start, 1]]
    visited[start] = 1
    while queue:
        now, cnt = queue.pop(0)
        for i in node[now]:
            if i and visited[i] == 0:
                if i == G:
                    return cnt
                queue.append((i, cnt+1))
                visited[i] = 1
    return 0

T = int(input())
for t in range(T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V+1)]
    for e in range(E):
        start, end = map(int, input().split())
        node[start].append(end)
        node[end].append(start)
    S, G = map(int, input().split())
    print(f'#{t+1}', bfs(V, S))