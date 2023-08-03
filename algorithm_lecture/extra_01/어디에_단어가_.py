import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    puzzle = []
    for i in range(N):
        puzzle.append(list(map(int, input().split())))
    
    rlt = 0

    cnt = 0
    for i in range(N):
        for j in range(N):
            if puzzle[i][j] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt == K :
                if j == N - 1:
                    rlt += 1
                elif puzzle[i][j+1] != 1:
                    rlt += 1
    
    cnt = 0
    for i in range(N):
        for j in range(N):
            if puzzle[j][i] == 1 :
                cnt += 1
            else:
                cnt = 0
            if cnt == K :
                if j == N - 1:
                    rlt += 1
                elif puzzle[j+1][i] != 1:
                    rlt += 1
                

print(rlt)
                


    