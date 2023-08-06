import sys
sys.stdin = open('input.txt')

# T = int(input())
# for t in range(T):
#     N, M = map(int, input().split())
#     fly = []
#     for i in range(N):
#         fly.append(list(map(int, input().split())))
#     sum_max = 0
#     for i in range(N-M+1):
#         for j in range(N-M+1):
#             temp_sum = 0
#             for k in range(i, i+M):
#                 temp_sum += sum(fly[k][j:j+M])
#             if temp_sum > sum_max:
#                 sum_max = temp_sum
#     print(f'#{t+1}', sum_max)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    fly = []
    for i in range(N):
        fly.append(list(map(int, input().split())))
        temp_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            temp_cnt = 0
            for k in range(M):
                for l in range(M):
                    temp_cnt += fly[i+k][j+l]
            if temp_cnt > temp_max:
                temp_max = temp_cnt
    print(temp_max)
        