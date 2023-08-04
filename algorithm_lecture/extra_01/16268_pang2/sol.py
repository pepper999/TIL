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
                if N > i+dx[l] >= 0 and M > j+dy[l] >= 0:
                    cnt += poong[i+(dx[l])][j+(dy[l])]
            if cnt >= temp_max:
                temp_max = cnt
    print(f'#{t+1}', temp_max)