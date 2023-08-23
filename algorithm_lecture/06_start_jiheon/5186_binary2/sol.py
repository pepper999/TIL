import sys
sys.stdin = open('input.txt')

T = int(input())

def to_binary(num):
    ans = ''
    for i in range(1, 13):
        if num == 0:
            return ans
        if num - 1*(2 ** (-i)) >= 0:
            num -= 1*(2 ** (-i))
            ans = ans + '1'
        elif num - 1*(2 ** (-i)) < 0:
            ans = ans + '0'
    if num != 0:
        return 'overflow'
    else:
        return ans

for t in range(T):
    num = float(input())
    print(f'#{t+1}', to_binary(num))
