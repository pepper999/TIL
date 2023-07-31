T = int(input())

for _ in range(T):
    N = int(input())
    ls = list(map(int, input().split()))
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if ls[i] <= ls[j] and j-i > cnt:
                cnt = j-i
                break

    print(cnt)
