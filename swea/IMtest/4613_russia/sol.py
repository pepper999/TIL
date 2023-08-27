import sys
sys.stdin = open('input.txt')
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    min_flag = 10 ** 5
    for i in range(N-2):
        for j in range(N - 1 - i):
            cnt = 0
            for l in range(i+1):
                cnt += M - flag[l].count('W')
            for l in range(i+1, i + 1 + j):
                cnt += M - flag[l].count('B')
            for l in range(i + 1 + j, N):
                cnt += M - flag[l].count('R')
            min_flag = min(cnt, min_flag)
    print(f'#{t+1}', min_flag)
            
            
                

