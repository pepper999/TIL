import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    rlt = []
    N, M = map(int, input().split())
    num_ls = list(map(int, input().split()))
    c_ls = [sum(num_ls[:i]) for i in range(len(num_ls)+1)]
    for i in range(1, N-M+2):
        rlt.append(c_ls[i+M-1] - c_ls[i-1])
    print(f'#{_+1}', max(rlt) - min(rlt))