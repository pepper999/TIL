import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    pizza = deque(list(map(int, input().split())))
    fire = deque([])
    cnt = 1
    for i in range(N):
        fire.append([cnt, pizza.popleft()])
        cnt += 1
    while len(fire) > 1:
        check = fire.popleft()
        check[1] //= 2
        if check[1] == 0:
            if pizza:
                fire.append([cnt, pizza.popleft()])
                cnt += 1
        else:
            fire.append(check)
    print(f'#{t+1}', fire[0][0])
