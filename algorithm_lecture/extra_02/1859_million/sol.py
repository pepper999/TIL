import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    now_price = 0
    N = int(input())
    price = list(map(int, input().split()))
    max_price = price.pop(-1)
    while len(price) > 0:
        if max_price > price[-1]:
            now_price += max_price - price.pop(-1)
        elif max_price <= price[-1]:
            max_price = price.pop(-1)
    print(f'#{t+1}', now_price) 

