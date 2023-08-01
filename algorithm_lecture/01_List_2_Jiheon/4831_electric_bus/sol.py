import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(T):
    # K -> 한번에 이동가능, N -> 종착역 거리, M -> 주유가능 갯수(안중요)
    K, N, M = map(int, input().split())
    # 주유가능 역의 list
    ls = list(map(int, input().split()))
    # 종착역을 list 맨 뒤에 넣어서 종착역에 도착하는 경우의 수 확인가능
    ls.append(N)
    # now -> 현재 버스의 위치, i -> 주유가능한 i번째 역, cnt -> 주유 횟수
    now = 0
    i = 0
    cnt = 0
    # 버스의 현재위치가 종착역 이전일 경우 계속 반복
    while now < N:
    # 현재 위치에서 갈 수 있는 가장 먼 거리를 갔을 경우
        now += K
        # 만약 현재 위치가 종착역과 같거나 멀다면 도착
        if now >= ls[-1]:
            print(f'#{_+1}', cnt)
            break
        # 현재위치가 주유 가능한 가장 가까운 역에 갈 수 없다면 0 출력
        if now < ls[i]:
            print(f'#{_+1}', 0)
            break
        # 현재위치가 주유 가능한 가장 가까운 역에 갈 수 있다면, 가능한 역중 가장 먼 역에서 주유
        while now >= ls[i]:
            i += 1
        cnt += 1
        # 이전에 주유한 역에서 다시 출발한다고 가정
        now = ls[i-1]
