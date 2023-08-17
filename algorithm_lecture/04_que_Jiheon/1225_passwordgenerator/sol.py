import sys
sys.stdin = open('input.txt')

from collections import deque

def pw():
    password = deque(list(map(int, input().split())))
    while password[-1] > 0:
        for i in range(1, 6):
            password.append(password.popleft() - i)
            if password[-1] <= 0:
                password[-1] = 0
                return password
    return password

for _ in range(10):
    T = int(input())
    print(f'#{T}', *pw())