import sys
sys.stdin = open('input.txt')

def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(left_node[node])
    inorder(right_node[node])

T = int(input())
for t in range(T):
    E, N = map(int, input().split())
    node_ssang = list(map(int, input().split()))
    parents_node = [0] * E * 2
    left_node = [0] * E * 2
    right_node = [0] * E * 2
    for i in range(E):
        parents_node[node_ssang[i*2]] = node_ssang[i*2]
        if left_node[node_ssang[i*2]] == 0:
            left_node[node_ssang[i*2]] = node_ssang[i*2+1]
        else:
            right_node[node_ssang[i*2]] = node_ssang[i*2+1]
    
    cnt = 0
    inorder(N)
    print(f'#{t+1}', cnt)
    
