import sys
sys.stdin = open('input.txt')

	
T = int(input())
 
for t in range(T):
    N, M = map(int, input().split())
    ground = []
    for i in range(N):
        ground.append(list(map(int, input().split())))
     
    max_cnt = 0
    for i in range(N):
        cnt = 0
        for j in range(M):
            if ground[i][j] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt > max_cnt:
                max_cnt = cnt
     
    for j in range(M):
        cnt = 0
        for i in range(N):
            if ground[i][j] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt > max_cnt:
                max_cnt = cnt
     
    print(f'#{t+1}',max_cnt)