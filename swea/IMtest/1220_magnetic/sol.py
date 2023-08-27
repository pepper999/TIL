import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    mag = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if mag[j][i] == 1 and not stack:
                stack.append(1)
            elif mag[j][i] == 2:
                if stack:
                    stack.pop()
                    cnt += 1
    print(f'#{t}', cnt)