import sys
sys.stdin = open('input.txt')

# 간단한 중위순회 함수 작성
def inorder(now):
    if now <= N :
        inorder(now*2)
        print(node[now], end = '')
        inorder(now*2 + 1)

for t in range(10):
    N = int(input())
    # 그래프 순서대로 작성
    node = [0] * (N+1)
    # 노드를 각각 연결
    for i in range(N):
        temp = list(input().split())
        node[i+1] = temp[1]
    print(node)

    print(f'#{t+1}', end = ' ')
    # 중위순회 돌림
    inorder(1)
    print()



