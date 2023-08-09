import sys
sys.stdin = open('input.txt')

T = int(input())

def DFS(start, end):
    stack = []
    visited = [False] * (V+1)
    stack.append(start)

    while stack:
        now = stack.pop()
        visited[now] = True
        for i in range(1, V+1):
            if not visited[i] and node[now][i]:
                stack.append(i)
    if visited[end]:
        return 1
    else:
        return 0

for t in range(T):
    V, E = map(int, input().split())
    node = [[0 for i in range(V+1)] for j in range(V+1)]
    for _ in range(E):
        start, end = map(int, input().split())
        node[start][end] = 1
    start, end = map(int, input().split())
    print(f'#{t+1}', DFS(start, end))
        
        
