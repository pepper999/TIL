import sys
sys.stdin = open('input.txt')


for _ in range(10):
    N = int(input())
    ls = list(map(int, input().split()))
    rlt = 0
    for i in range(2, len(ls)-2):
        if ls[i] - ls[i-1] > 0 and ls[i] - ls[i+1] > 0 and ls[i] - ls[i-2] > 0 and ls[i] - ls[i+2] > 0:
            rlt += min(ls[i] - ls[i - 1], ls[i] - ls[i + 1], ls[i] - ls[i-2], ls[i] - ls[i+2])

    print(f'#{_+1}', rlt)
