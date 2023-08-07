import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    str = input()
    list = input()
    rlt = 0
    for i in range(len(list)-len(str)+1):
        if str == list[i:i+len(str)]:
            rlt = 1
    print(f'#{t+1}', rlt)
        