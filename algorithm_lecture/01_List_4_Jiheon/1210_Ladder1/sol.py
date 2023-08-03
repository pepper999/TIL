import sys
import pprint
sys.stdin = open('input.txt')

for _ in range(10):
    T = input()
    radder = []
    for _ in range(100):
        radder.append(list(map(int, input().split())))
    for i in range(100):
        if radder[0][i] == 1:
            x, y = 0, i
            while x < 99:
                x += 1
                if y > 0 and radder[x][y-1] == 1:
                    while y > 0 and radder[x][y-1] == 1:
                        y -= 1
                elif y < 99 and radder[x][y+1] == 1:
                    while y < 99 and radder[x][y+1] == 1:
                        y += 1
            if radder[x][y] == 2:
                result = i
                break
    print(f'#{T}', result)
