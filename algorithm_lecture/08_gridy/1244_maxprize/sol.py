import sys
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    global rlt
    if cnt == time:
        rlt = max(int(''.join(nums)), rlt)
        return
    for i in range(idx, len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] <= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i, cnt + 1)
                nums[i], nums[j] = nums[j], nums[i]
    if not rlt and cnt < time:
        if (time - cnt) % 2:
            nums[-1], nums[-2] = nums[-2], nums[-1]
        dfs(idx, int(time))

T = int(input())
for t in range(T):
    nums, time = input().split()
    nums = list(nums)
    time = int(time)
    rlt = 0
    dfs(0, 0)
    print(f'#{t+1}', rlt)
    