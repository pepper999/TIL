
def triangle(N):
    triangle = []
    for i in range(N):
        triangle.append([1]*(i + 1))
        if i >= 2:
            for j in range(1, i):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
    return triangle
T = int(input())
for t in range(T):
    N = int(input())
    tri = triangle(N)
    print(f'#{t+1}')
    for i in range(N):
        print(*tri[i])