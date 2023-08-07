import sys
sys.stdin = open('input.txt')

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
counting = [0]*10

T = int(input())
for t in range(T):
    t, N = input().split()
    N = int(N)
    str = list(input().split())
    for i in range(N):
        counting[num.index(str[i])] += 1
    sorted_str = []
    for i in range(10):
        while counting[i] > 0:
            sorted_str.append(num[i])
            counting[i] -= 1
    print(t)
    print(*sorted_str)