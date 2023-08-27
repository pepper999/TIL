T = int(input())
for t in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    temp_max = 0
    for i in range(N-1):
        for j in range(i+1, N):
            danjo = list(str(nums[i] * nums[j]))
            flag = 1
            for k in range(len(danjo)-1):
                if danjo[k] > danjo[k+1]:
                    flag = 0
                    break
            if flag == 1:
                if temp_max < int(''.join(danjo)):
                    temp_max = int(''.join(danjo))
    if temp_max != 0:                    
        print(f'#{t+1}', temp_max)
    else:
        print(f'#{t+1}', -1)