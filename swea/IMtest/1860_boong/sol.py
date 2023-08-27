import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M, K = map(int, input().split())
    sec = list(map(int, input().split()))
    sec.sort()
    now = M
    now_cnt = 0
    rlt = 1
    for i in range(N):
        if now_cnt == 0:
            if sec[i] < now:
                print(f'#{t+1}','Impossible')
                rlt = 0
                break
            else:
                now_cnt += K - 1
                now += M
        else:
            now_cnt -= 1
    if rlt == 1:
        print(f'#{t+1}','Possible')