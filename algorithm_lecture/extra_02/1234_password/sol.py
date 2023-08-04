import sys
sys.stdin = open('input.txt')

for t in range(10):
    N, str = input().split()
    N = int(N)
    str = list(str)
    i = 0
    while len(str) > i + 1:
        while len(str) > i + 1 and str[i] == str[i+1]:
            str.pop(i)
            str.pop(i)
            i -= 1
        else:
            i += 1
    
    print(f'#{t+1}', ''.join(str))