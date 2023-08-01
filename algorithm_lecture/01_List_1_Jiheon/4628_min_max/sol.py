import sys

sys.stdin = open('4628minmax/input.txt')

T = int(input())
for i in range(T):
	N = int(input())
	ls = list(map(int, input().split()))
	temp_max, temp_min = 0, ls[0]
	for j in range(N):
		if ls[j] > temp_max:
			temp_max = int(ls[j])
		if ls[j] < temp_min:
			temp_min = int(ls[j])
	print(f'#{i+1}', temp_max - temp_min)
