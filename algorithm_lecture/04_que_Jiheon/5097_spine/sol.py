import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    for i in range(M):
        nums.append(nums.popleft())
    print(f'#{t+1}', nums[0])
