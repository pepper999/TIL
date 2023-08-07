import sys
sys.stdin = open('input.txt')

def palindrome(str):
    mid = len(str) // 2
    for i in range(mid):
        if str[i] != str[-i-1]:
            return 0
    return 1

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    str = [input() for _ in range(N)]
    col_str = list(zip(*str))
    for i in range(N):
        for j in range(N-M+1):
            if palindrome(str[i][j:j+M]) == 1:
                print(f'#{t+1}', ''.join(str[i][j:j+M]))
                break
            if palindrome(col_str[i][j:j+M]) == 1:
                print(f'#{t+1}', ''.join(col_str[i][j:j+M]))
                break

            
    
