import sys
sys.stdin = open('input.txt')

T = int(input())

def forth():
    stack = []
    input_list = list(input().split())
    for i in range(len(input_list)-1):
        if input_list[i] not in '+-*/.':
            stack.append(input_list[i])
        elif len(stack) >= 2:
            num1 = int(stack.pop())
            num2 = int(stack.pop())
            if input_list[i] == '+':
                stack.append(num1 + num2)
            elif input_list[i] == '-':
                stack.append(num2 - num1)
            elif input_list[i] == '/':
                stack.append(int(num2//num1))
            else:
                stack.append(num1 * num2)
        else:
            return 'error'
    if len(stack) == 1:
        return stack[0]
    else:
        return 'error'

for t in range(T):
    print(f'#{t+1}', forth())