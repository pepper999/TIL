import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    max_sum = 0
    for i in range(K):
        temp_max = 0
        for i in range(len(scores)):
            if scores[i] > temp_max:
                temp_max = scores[i]
        max_sum += temp_max
        scores.remove(temp_max)
    print(max_sum)

        