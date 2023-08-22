import sys
sys.stdin = open('input.txt')

def binaryheap(tree):
    for i in range(1, len(tree)):
        while tree[i//2] > tree[i]:
            tree[i//2], tree[i] = tree[i], tree[i//2]
            i //= 2

T = int(input())
for t in range(T):
    N = int(input())
    tree = [0] + list(map(int, input().split()))
    binaryheap(tree)
    sum_value = 0
    while N:
        N //= 2
        sum_value += tree[N]
    print(f'#{t+1}',sum_value)