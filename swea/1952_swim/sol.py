import sys
sys.stdin = open('input.txt')

def dfs(start, total):
    global temp_min
    if total > temp_min:
        return
    if start >= 12:
        temp_min = min(temp_min, total)
        return
    days = plan[start]
    dfs(start + 1, total + (day * days))
    dfs(start + 1, total + month)
    dfs(start + 3, total + quarter)
    dfs(start + 12, total + year)
    return temp_min



T = int(input())
for t in range(T):
    day, month, quarter, year = map(int, input().split())
    plan = list(map(int, input().split()))
    temp_min = float('inf')
    print(f'#{t+1}', dfs(0, 0))