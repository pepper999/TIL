import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(T):
    P, A, B = map(int, input().split())
    end_A = P
    end_B = P
    start_A = 1
    start_B = 1
    cnt_A = 0
    cnt_B = 0

# A 와 B 각각의 이진탐색 경우를 구해, 횟수를 따로 도출
    while start_A <= end_A:
        mid = (end_A + start_A)//2
        if mid > A:
            end_A = mid
            cnt_A += 1
        elif mid < A:
            start_A = mid
            cnt_A += 1
        elif mid == A:
            break

    while start_B <= end_B:
        mid = (end_B + start_B)//2
        if mid > B:
            end_B = mid
            cnt_B += 1
        elif mid < B:
            start_B = mid
            cnt_B += 1
        elif mid == B:
            break
    
    if cnt_A > cnt_B:
        win = 'B'
    elif cnt_A < cnt_B:
        win = 'A'
    else:
        win = 0
    print(f'#{t+1}', win)


