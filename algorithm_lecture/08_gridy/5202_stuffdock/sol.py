import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    period = [list(map(int, input().split())) for _ in range(N)]
    period.sort(key = lambda x : (x[1], x[0]))
    cnt = 0
    end_time = 0
    for i in range(N):
        if period[i][0] >= end_time:
            end_time = period[i][1]
            cnt += 1
    print(f'#{t+1}', cnt)