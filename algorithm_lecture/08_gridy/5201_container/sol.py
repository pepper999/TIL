import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    stuff = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    truck.sort(reverse=True)
    stuff.sort(reverse=True)
    dp = [0] * M
    for i in range(len(truck)):
        for j in range(len(stuff)):
            if truck[i] >= stuff[j] and dp[i] < stuff[j]:
                dp[i] = stuff.pop(stuff.index(stuff[j]))
                break
    print(sum(dp))