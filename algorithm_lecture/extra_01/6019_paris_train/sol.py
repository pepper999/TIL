T = int(input())
for t in range(T):
    D, A, B, F = map(int, input().split())
    time = D/(A+B)
    print(f'#{t+1}', F*time)