T = int(input())
for t in range(T):
    N = int(input())
    AB = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    P = int(input())

    num_bus = [0] * P
    for i in range(P):
        a = input()
    
    for i in AB:
        for j in range(i[0]-1, i[1]):
            num_bus[j] += 1
    
    print(f'#{t+1}', *num_bus)

    