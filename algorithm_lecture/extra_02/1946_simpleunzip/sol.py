import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N = int(input())
    ip_list = []
    str = []
    for i in range(N):
        alpha, num = input().split()
        str = str + [alpha * int(num)]
    str = ''.join(str)
    print(f'#{t+1}')
    for i in range(0, len(str), 10):
        print(str[i:i+10])
    