import sys
sys.stdin = open('input.txt')

# T = int(input())
# for t in range(T):
#     N = int(input())
#     num = list(map(int, input().split()))
#     num.sort()
#     special_sort = [0] * N
#     mid = int(N/2)
#     for i in range(1, mid+1):
#         special_sort[i*2 - 1] = num[i - 1]
#     for i in range(mid):
#         special_sort[i*2] = num[-i-1]
#     print(f'#{t+1}', end = ' ')
#     for i in range(N):
#         print(special_sort[i], end = ' ')
#         print()

T = int(input())
for t in range(T):

    N = int(input())
    num = list(map(int, input().split()))
    num.sort()
    rlt = []
    for i in range(5):
            rlt.append(num.pop(-1))
            rlt.append(num.pop(0))
    print(f'#{t+1}', *rlt)


# def select(list, n):
#     for i in range(n):
#         minindex = i
#         for j in range(i+1, len(list)):
#             if list[minindex] > list[j]:
#                 minindex = j
#         list[i], list[minindex] = list[minindex], list[i]
#         return list[n-1]