import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    n = int(input())
    a = [list(map(int, input().split())) for j in range(n)]
    a_90 = [[0 for j in range(n)] for j in range(n)]
    a_180 = [[0 for j in range(n)] for j in range(n)]
    a_270 = [[0 for j in range(n)] for j in range(n)]
    
    for j in range(n):
        for k in range(n):
            a_90[j][k] = a[n-k-1][j]
    for j in range(n):
        for k in range(n):
            a_180[j][k] = a_90[n-k-1][j]
    for j in range(n):
        for k in range(n):
            a_270[j][k] = a_180[n-k-1][j]
            
    print(f'#{i+1}')
    for j in range(n):
        for k in range(n):
            print(a_90[j][k], end='')
        print(end = ' ')
        for k in range(n):
            print(a_180[j][k], end='')
        print(end = ' ')
        for k in range(n):
            print(a_270[j][k], end='')
        print()
    