import sys
sys.stdin = open('input.txt')

for T in range(1, 11):
    N = int(input())
    a = input()
    stack = []
    new_stack = []

    for x in a:
        if x.isdecimal():
            new_stack.append(x)
        else:
            if x == '(':
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    new_stack.append(stack.pop())
                stack.pop()

            elif x == '*':
                while stack and stack[-1] == '*':
                    new_stack.append(stack.pop())
                stack.append(x)
            elif x == '+':
                while stack and stack[-1] != '(':
                    new_stack.append(stack.pop())
                stack.append(x)

    while stack:
        new_stack.append(stack.pop())

    for i in range(len(new_stack)):
        if new_stack[i].isdecimal():
            stack.append(int(new_stack[i]))
        else:
            x, y = stack.pop(), stack.pop()
            if new_stack[i] == '+':
                stack.append(x + y)
            elif new_stack[i] == '*':
                stack.append(x * y)

    print(f'#{T} {stack[0]}')
