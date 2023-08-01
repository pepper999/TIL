import sys
sys.stdin = open('input.txt')

def counting_sort(list, k):
    c_list = [0] * (k + 1)
    result = [-1] * len(list)
    for i in range(len(list)):
        c_list[list[i]] += 1
    for i in range(1, len(c_list)):
        c_list[i] += c_list[i-1]
    for i in list:
        c_list[i] -= 1
        result[c_list[i]] = i
    return result
 
for _ in range(10):
    N = int(input())
    ls = list(map(int, input().split()))
    ls = counting_sort(ls, 100)
    for i in range(N):
        ls[0] += 1
        ls[-1] -= 1
        ls = counting_sort(ls, 100)
    print(f'#{_+1}', ls[-1] - ls[0])