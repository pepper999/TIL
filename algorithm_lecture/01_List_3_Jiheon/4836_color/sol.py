import sys
sys.stdin = open('input.txt')
import pprint

# T = int(input())
# for t in range(T):
#     N = int(input())
# # 도화지로 쓸 paper 2차원 리스트 형성
#     paper = [[0]*10 for i in range(10)]
#     for i in range(N):
#         ls = list(map(int, input().split()))
#         # 입력 리스트의 마지막 값을 확인하여 색칠할 색깔 확인
#         if ls[-1] == 1:
#             # 주어진 x좌표, y좌표를 들고옴
#             for j in range(ls[0], ls[2]+1):
#                 for k in range(ls[1], ls[3]+1):
#                     # 종이가 안칠해져있다면(0 -> 초기값)
#                     if paper[j][k] == 0:
#                         # 1을 칠함
#                         paper[j][k] = 1
#                     # 종이에 다른색이 칠해져 있다면 섞인색(3)이 칠해지도록 함
#                     elif paper[j][k] == 2:
#                         paper[j][k] = 3
#         elif ls[-1] == 2:
#             for j in range(ls[0], ls[2]+1):
#                 for k in range(ls[1], ls[3]+1):
#                     if paper[j][k] == 0:
#                         paper[j][k] = 2
#                     elif paper[j][k] == 1:
#                         paper[j][k] = 3
#     cnt = 0
#     for i in range(10):
#         cnt += paper[i].count(3)
#     print(f'#{t+1}', cnt)

T = int(input())
for t in range(T):
    N = int(input())
    paper = [[0] * 10 for _ in range(10)]
    for i in range(N):
        query = list(map(int, input().split()))

        if query[-1] == 1:
            for j in range(query[0], query[2]+1):
                for k in range(query[1], query[3]+1):
                    if paper[j][k] == 0:
                        paper[j][k] = 1
                    elif paper[j][k] == 2:
                        paper[j][k] = 3
        else:
            for j in range(query[0], query[2]+1):
                for k in range(query[1], query[3]+1):
                    if paper[j][k] == 0:
                        paper[j][k] = 2
                    elif paper[j][k] == 1:
                        paper[j][k] = 3
    cnt = 0
    for i in range(10):
        cnt += paper[i].count(3)
    print(cnt)