N = int(input())
if N == 1:
    print(0)
for i in range(1, N+1):
    num = i + sum(list(map(int, str(i))))
    if num == N:
        print(i)
        break
if num != N:
        print(0)
    
    