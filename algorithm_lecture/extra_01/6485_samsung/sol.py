T = int(input())
for t in range(T):
    N = int(input())
    AB = []
    station = []
    for i in range(N):
        AB.append(list(map(int, input().split())))
    
    P = int(input())

    for i in range(P):
        num = int(input())
        station.append([num, 0])
    
    for i in AB:
        for j in range(i[0], i[1]+1):
            for k in range(len(station)):
                if station[k][0] == j:
                    station[k][1] += 1
    
    print(f'#{t+1}', end = ' ')
    for i in range(len(station)):
        print(station[i][1], end =  ' ')
    print()

    