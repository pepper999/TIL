import sys
sys.stdin = open('input.txt')

def dfs(N, start):
    stack = [start]
    visited = [0] * (N+1)
    while stack:
        now = stack.pop()
        if now == 99:
            return 1
        if visited[now] == 0:
            visited[now] = 1
        for i in node[now]:
            if visited[i] == 0:
                stack.append(i)
    return 0
    
    
for tc in range(10):
    t, N = map(int, input().split())
    node = [[] for _ in range(101)]
    route = list(map(int, input().split()))
    for i in range(N):
        end = route.pop()
        start = route.pop()
        node[start].append(end)
    rlt = dfs(101, 1)
    print(f'#{t}', rlt)