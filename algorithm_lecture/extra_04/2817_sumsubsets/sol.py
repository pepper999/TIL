import sys
sys.stdin = open('input.txt')

def subset(idx, sum):
    global cnt
    if idx >= N:
        return
    temp = sum + nums[idx]
    if temp == K:
        cnt += 1
    
    subset(idx + 1, sum)
    subset(idx + 1, temp)

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0
    subset(0, 0)
    print(f'#{t+1}', cnt)