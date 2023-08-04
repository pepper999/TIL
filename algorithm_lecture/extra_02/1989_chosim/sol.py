import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    str = input()
    if str == str[::-1]:
        rlt = 1
    else:
        rlt = 0
    print(f'#{t+1}', rlt)