import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    str = input()
    stack = []
    for i in range(len(str)-1, -1, -1):
        stack.append(str[i])
        if len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
    if stack:
        print(len(stack))
    else:
        print(0)