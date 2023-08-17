def isroom(start, end):
    global cnt
    for i in range((start // 2) + (start % 2), (end // 2) + (end % 2) + 1):
        visited[i] += 1

T = int(input())
for t in range(T):
    N = int(input())
    visited = [0] * 201
    cnt = 1
    for i in range(N):
        start, end = map(int, input().split())
        if start <= end :
            isroom(start, end)
        else:
            isroom(end, start)
    print(f'#{t+1}', max(visited))