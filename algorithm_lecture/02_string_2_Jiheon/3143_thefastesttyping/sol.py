import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    A, B = input().split()
    i = 0
    cnt = 0
    while i < len(A):
        if A[i:i+len(B)] == B:
            cnt += 1
            i += len(B)
        else:
            cnt += 1
            i += 1
    print(f'#{t+1}',cnt)
