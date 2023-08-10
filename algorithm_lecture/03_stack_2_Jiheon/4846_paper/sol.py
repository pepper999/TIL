import sys
sys.stdin = open('input.txt')

# def paper(N):
#     if N == 10:
#         return 1
#     elif N == 20:
#         return 3
#     else:
#         return paper(N-10)+(2*paper(N-20))

# T = int(input())
# for t in range(T):
#     N = int(input())
#     rlt = paper(N)
#     print(f'#{t+1}', rlt)

def paper(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        cnt_list = [0] * int(N/10)
        cnt_list[0] = 1
        cnt_list[1] = 3
        for i in range(2, int(N/10)):
            cnt_list[i] = cnt_list[i-1] + (2*cnt_list[i-2])
        return cnt_list[-1]

T = int(input())
for t in range(T):
    N = int(input())
    rlt = paper(N)
    print(f'#{t+1}', rlt)
