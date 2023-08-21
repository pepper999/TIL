import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M, L = map(int, input().split())
    tree = [0] * (N+1)
    for i in range(M):
        node, val = map(int, input().split())
        tree[node] = val
    for i in range(N, 0, -1):
        if tree[i] == 0 and 2*i + 1 < N+1:
            tree[i] = tree[2*i] + tree[2 * i + 1]
        elif tree[i] == 0:
            tree[i] = tree[2*i]
    print(f'#{t+1}', tree[L])