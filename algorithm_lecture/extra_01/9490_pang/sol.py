import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    poong = []
    temp_max = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for n in range(N):
        poong.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(M):
            cnt = poong[i][j]
            for l in range(4):
                for k in range(1, poong[i][j]+1):
                    if N > i+dx[l]*k >= 0 and M > j+dy[l]*k >= 0:
                        cnt += poong[i+(dx[l]*k)][j+(dy[l]*k)]
            if cnt >= temp_max:
                temp_max = cnt
    print(f'#{t+1}', temp_max)

    
    