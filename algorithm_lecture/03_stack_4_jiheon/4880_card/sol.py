def half_half(start, end):
    if start == end:
        return start
    mid = (start + end) // 2
    left = half_half(start, mid)
    right = half_half(mid + 1, end)
    return the_rock(left, right)

def the_rock(left, right):
    if card[left] == card[right]:
        return left
    elif card[left] - card[right] == 1 or card[left] - card[right] == -2:
        return left
    return right

T = int(input())
for t in range(T):
    N = int(input())
    card = list(map(int, input().split()))
    print(f'#{t+1} {half_half(0, N-1)+1}')