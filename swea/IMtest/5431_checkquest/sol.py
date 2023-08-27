import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    quest = list(map(int, input().split()))
    print(f'#{t+1}', end = ' ')
    for i in range(1, N+1):
        if i not in quest:
            print(i, end = ' ')
    print()