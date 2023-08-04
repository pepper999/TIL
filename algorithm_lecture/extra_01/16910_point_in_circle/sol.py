T = int(input())
for t in range(T):
    N = int(input())
    num_list = [i for i in range(-N, N+1)]
    cnt = 0
    for x in num_list:
        for y in num_list:
            if x ** 2 + y ** 2 <= N ** 2:
                cnt += 1
    print(f'#{t+1}', cnt)