import sys
sys.stdin = open('input.txt')

def boong(N, M, K):
    for i in range(N):
        if (arrive[i] // M) * K - (i+1) < 0:
            return 'Impossible'
    return 'Possible'

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    arrive.sort()
    print(f'#{t+1}', boong(N, M, K))