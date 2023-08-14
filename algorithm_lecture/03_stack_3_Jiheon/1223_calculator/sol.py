import sys
sys.stdin = open('input.txt')

def calculator(arr):
    stack = []
    present = []
    for i in range(len(arr)):
        if arr[i] not in '+*':
            present.append(arr[i])
        elif arr[i] == '*':
            while stack and stack[-1] == '*':
                present.append(stack.pop())
            stack.append(arr[i])
        elif arr[i] == '+':
            while stack:
                present.append(stack.pop())
            stack.append(arr[i])
    while stack:
        present.append(stack.pop())

    for i in present:
        if i in '+*':
            num1 = stack.pop()
            num2 = stack.pop()
            if i == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)      
        else:  
            stack.append(int(i))
    return stack[0]

for t in range(10):
    N = int(input())
    num_list = list(input())
    print(f'#{t+1}', calculator(num_list))
