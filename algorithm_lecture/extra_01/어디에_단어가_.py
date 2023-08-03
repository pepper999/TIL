T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    
    rlt = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt == K :
                if j == N - 1:
                    rlt += 1
                    cnt = 0
                elif puzzle[i][j+1] != 1:
                    rlt += 1
                    cnt = 0
    
    for j in range(N):
        cnt = 0
        for i in range(N):
            if puzzle[i][j] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt == K :
                if i == N - 1:
                    rlt += 1
                    cnt = 0
                elif puzzle[i+1][j] != 1:
                    rlt += 1
                    cnt = 0
    
    print(rlt)
                


    