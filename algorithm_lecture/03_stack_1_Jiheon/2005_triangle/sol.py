def triangle(N):
    triangle = []
    stack = []
    for i in range(N):
        triangle = [1]*(i + 1)
        if i >= 2:
            for j in range(1, i):
                triangle[j] = stack[-1][j-1] + stack[-1][j]
        stack.append(triangle)
    return stack
T = int(input())
for t in range(T):
    N = int(input())
    tri = triangle(N)
    print(f'#{t+1}')
    for i in range(N):
        print(*tri[i])