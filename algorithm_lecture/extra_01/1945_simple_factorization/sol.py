import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    abcde = {2:0, 3:0, 5:0, 7:0, 11:0}
    N = int(input())
    for i in abcde.keys():
        while N % i == 0 :
            abcde[i] += 1
            N /= i
    print(f'#{t+1}', *abcde.values())
    