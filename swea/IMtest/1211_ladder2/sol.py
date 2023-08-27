import sys
sys.stdin = open('input.txt')

def game(x, y):
    cnt = 0
    while x < 99:
        x += 1
        cnt += 1
        if 0 <= y-1 and radder[x][y-1]:
            while 0 <= y - 1 and radder[x][y - 1]:
                y -= 1
                cnt += 1
        elif y + 1 < 100 and radder[x][y + 1]:
            while y + 1 < 100 and radder[x][y + 1]:
                y += 1
                cnt += 1
    return cnt
    

for _ in range(10):
    t = int(input())
    radder = [list(map(int, input().split())) for _ in range(100)]
    rlt = []
    for i in range(100):
        if radder[0][i] == 1:
            rlt.append([game(0, i), i])
    print(f'#{t}', min(rlt)[1])