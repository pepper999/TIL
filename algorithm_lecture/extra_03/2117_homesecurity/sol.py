import sys
sys.stdin = open('input.txt')

def securityarea(x, y, k):
    k -= 1
    temp_sum = 0
    cnt = 0
    for i in range(y - k, y + k + 1):
        for j in range(x + abs(k - i),  2 * k - 1 - abs(k - i)):
            if 0 <= i < N and 0 <= j < N:
                temp_sum += city[i][j] * M
                if city[i][j] == 1:
                    cnt += 1
    return temp_sum, cnt


T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp_bill, cnt = securityarea(i, j, k)
                if temp_bill > k * k + (k-1) * (k-1):
                    max_cnt = max(max_cnt, cnt)
    print(max_cnt)