import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    string = [list(input()) for _ in range(5)]
    print(f'#{t+1}', end = ' ')
    for i in range(15):
        for j in range(5):
            if i < len(string[j]):
                print(string[j][i], end = '')
    print()
