import sys
sys.stdin = open('input.txt')

num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
for t in range(T):
    t, N = input().split()
    N = int(N)
    str = list(input().split())
    for i in range(N):
        str[i] = num.index(str[i])
    str.sort()
    for i in range(N):
        str[i] = num[str[i]]
    print(t)
    print(*str)