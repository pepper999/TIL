import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    def palindrome():
        N, M = map(int, input().split())
        str = [input() for _ in range(N)]
        col_str = list(zip(*str))
        for i in range(N):
            for j in range(N-M+1):
                if str[i][j:j+M] == str[i][j:j+M][::-1]:
                    print(f'#{t+1}', ''.join(str[i][j:j+M]))
                    return        
                if col_str[i][j:j+M] == col_str[i][j:j+M][::-1]:
                    print(f'#{t+1}', ''.join(col_str[i][j:j+M]))
                    return


    palindrome()

