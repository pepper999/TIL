import sys
sys.stdin = open('input.txt')

T = int(input())

def to_binary(num):
    ans = ''
    for i in range(4):
        ans = str(num % 2) + ans
        num //= 2
    return ans

def hex_to_binary(num):
    ans = ''
    for str in num:
        if str.isdigit():
            ans += to_binary(int(str))
        else:
            ans += to_binary(hex_num[str])
    return ans

hex_num = {'A' : 10, 'B' : 11, 'C' : 12, 'D' : 13, 'E' : 14, 'F' : 15}

for t in range(T):
    n, num = input().split()
    print(f'#{t+1}', hex_to_binary(num))