import sys
sys.stdin = open('input.txt')

for _ in range(10):
    N = int(input())
    ls = list(map(int, input().split()))
    for i in range(N):
        ls[ls.index(max(ls))] -= 1
        ls[ls.index(min(ls))] += 1
    print(f'#{_+1}', max(ls) - min(ls))
