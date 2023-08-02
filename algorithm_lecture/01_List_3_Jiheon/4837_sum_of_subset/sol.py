import sys
sys.stdin = open('input.txt')

# T = int(input())

# subset_list = [[]]
# for i in range(1, 13):
#         size = len(subset_list)
#         for j in range(size):
#             subset_list.append(subset_list[j]+[i])

# for t in range(T):
#     N, K = map(int, input().split())
#     cnt = 0
#     for i in range(len(subset_list)):
#         if len(subset_list[i]) == N and sum(subset_list[i]) == K:
#             cnt += 1
#     print(f'#{t+1}', cnt)

T = int(input())

list = [i for i in range(1, 13)]

for t in range(T):
    N, K = map(int, input().split())

    n = len(list)
    cnt = 0
    for i in range(1 << n):
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(list[j])
        if len(subset) == N and sum(subset) == K:
            cnt += 1
    print(f'#{t+1}', cnt)