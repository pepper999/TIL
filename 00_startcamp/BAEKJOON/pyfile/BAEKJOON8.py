# 2869 달팽이

import math

A, B, V = map(int, input().split())

N = math.ceil((V-A)/(A-B))

print(N + 1)


# 1193 분수찾기

num = int(input())

line = 1
while line < num:
    num-=line
    line+=1

if line%2 == 0:
    rlt = num, line-num+1
    
if line%2 == 1:
    rlt = line-num+1, num
    
print(rlt[0], end='')
print('/', end = '')
print(rlt[1], end = '')
print()
        
        

