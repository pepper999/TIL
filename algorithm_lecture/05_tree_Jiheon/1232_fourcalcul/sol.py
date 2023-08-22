import sys
sys.stdin = open('input.txt')

def postorder(now):
    if now:
        postorder(left[now])
        postorder(right[now])
        if node[now] == '+':
            node[now] = int(node[left[now]]) + int(node[right[now]])
        elif node[now] == '-':
            node[now] = int(node[left[now]]) - int(node[right[now]])
        elif node[now] == '*':
            node[now] = int(node[left[now]]) * int(node[right[now]])
        elif node[now] == '/':
            node[now] = int(node[left[now]]) // int(node[right[now]])

for t in range(10):
    N = int(input())
    node = [0] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        temp_input = input().split()
        node[int(temp_input[0])] = temp_input[1]
        if len(temp_input) == 4:
            left[int(temp_input[0])] = int(temp_input[2])
            right[int(temp_input[0])] = int(temp_input[3])
    print(node)
    postorder(1)
    print(f'#{t+1}', node[1])