import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    stick = input()
    now = 0
    total = 0
    for i in range(len(stick)):
        if stick[i] == '(' and stick[i+1] != ')':
            now += 1
        elif stick[i] == '(' and stick[i+1] == ')':
            total += now
        elif stick[i] == ')' and stick[i-1] != '(':
            now -= 1
            total += 1
    print(f'#{t+1}', total)
        