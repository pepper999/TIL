# 백준 단계별로 풀어보기 (7 - 9)
### 백준 7단계
### 백준 8단계
- 2869 달팽이
```python
import math

A, B, V = map(int, input().split())

N = math.ceil((V-A)/(A-B))

print(N + 1)
```
- 1193 분수찾기
```python
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
```

### 백준 9단계
- 5086 배수
```python
num1, num2 = 2, 2
while num1 != 0 and num2 != 0:
    num1, num2 = map(int, input().split())

    if num1 > num2 and num1%num2 == 0:
        print('multiple')
    elif num1 < num2 and num2%num2 == 0:
        print('factor')
    elif num1 != 0 and num2 != 0:
        print('neither')
    else:
      break
```
- 2501 약수 구하기
```python
N, K = map(int, input().split())
ls = [0]*N
for i in range(1, N+1):
    if N%i == 0 :
        ls[i-1] = i
for i in range(len(ls)):
    try:
        ls.remove(0)
    except:
        break

try:
    print(ls[K-1])
except:
    print(0)
```
- 9506 약수들의 합
```python
n = 0
ls = [6, 28, 496, 8128, 33550336]
while n != -1:
    ls2 = []
    prints = []
    n = int(input())
    if n in ls:
        for i in range(1, n+1):
            if n%i == 0:
                ls2.append(i)
        print(n,'=', end = ' ')
        for j in range(len(ls2)):
            prints.append(ls2[j])
            prints.append('+')
        for j in range(len(prints)-3):
            print(prints[j], end = ' ')
        print()
    elif n == -1:
        break
    else:
        print(n, 'is NOT perfect.')
```
- 1978 소수 찾기
```python
n = int(input())
num = list(map(int, input().split()))
pnt = 0
for i in range(n):
    rlt = 0
    for j in range(2, num[i]):
        if num[i]%j != 0:
            rlt += 1
    if rlt == num[i]-2:
        pnt += 1
```
- 2581 소수
```python
M = int(input())
N = int(input())

ls = [i+M for i in range(N-M+1)]
ls_ = []

for i in range(len(ls)):
    if ls[i] == 1:
        ls[i] = 0
    for j in range(ls_):
        if ls[i]%j == 0:
            ls[i] = 0
            break
        else:
            pass
ls = [item for item in ls if item != 0]
if len(ls) > 1:
    print(sum(ls))
    print(min(ls))
else :
    print(-1)
```
- 11653 소인수 분해
```python
num = int(input())

for i in range(2, num+1):
    while num%i == 0:
        num = num/i
        print(i)
    else:
        pass
```