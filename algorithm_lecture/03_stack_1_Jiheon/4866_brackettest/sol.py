import sys
sys.stdin = open('input.txt')

def bracket(str):
    for i in range(len(str)):
        if str[i] == '{':
            stack.append('{')
        elif str[i] == '(':
            stack.append('(')
        elif str[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif str[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                return 0
    if stack:
        return 0
    else:
        return 1

T = int(input())
for t in range(T):
    str = input()
    stack = []
    print(f'#{t+1}', bracket(str))
    