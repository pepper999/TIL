import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    farm = [list(map(int, list(input()))) for _ in range(N)]
    mid = N // 2
    temp_sum = 0
    for i in range(N):
        start = abs(mid - i)
        temp_sum += sum(farm[i][start:N - start])
    print(f'#{t+1}', temp_sum)
        