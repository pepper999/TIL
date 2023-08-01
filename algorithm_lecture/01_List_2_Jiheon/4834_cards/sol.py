import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    # card_max -> card count 값중 가장 큰 값
    card_max = 0
    # card_num -> card_max 값의 카드 숫자
    card_num = 0
    N = int(input())
    card = list(map(int, list(str(input()))))
    for i in range(N):
        card_count = card.count(card[i])
        if card_count > card_max:
            card_max = int(card_count)
            card_num = card[i]
        elif card_count == card_max:
            if card[i] > card_num:
                card_num = card[i]
    print(f'#{_+1}', card_num, card_max)
