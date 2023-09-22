import sys
sys.stdin = open('input.txt')

def find(a):
    if parents[a] != a:
        parent = parents[a]
        parents[a] = find(parent)
        weight[a] += weight[parent]
    return parents[a]

def union(a, b, w):
    pa = find(a)
    pb = find(b)
    if ranks[pa] > ranks[pb]:
        parents[pb] = pa
        weight[pb] = weight[a] - weight[b] + w
    elif ranks[pa] < ranks[pb]:
        parents[pa] = pb
        weight[pa] = weight[b] - weight[a] - w
    else:
        parents[pa] = pb
        weight[pa] = weight[b] - weight[a] - w
        ranks[pb] += 1

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    parents = [i for i in range(N + 1)]
    ranks = [0] * (N+1)
    weight = [0] * (N + 1)
    rlt = []
    for _ in range(M):
        query, *sample = input().split()
        if query == '!':
            a, b, w = map(int, sample)
            union(a, b, w)
        else:
            a, b = map(int, sample)
            if find(a) == find(b):
                rlt.append(weight[b] - weight[a])
            else:
                rlt.append('UNKNOWN')
    print(f'#{t+1}', *rlt) 
