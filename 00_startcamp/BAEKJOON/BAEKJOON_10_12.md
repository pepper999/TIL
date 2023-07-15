# 백준 단계별로 풀어보기(10-12)
### 백준 10단계
- 3009 네번째 점
```python
a_ls = []
b_li = []
rlt = [0,0]
for i in range(3):
    a, b = map(int, input().split())
    a_ls.append(a)
    b_ls.append(b)

for i in range(3):
    if a_ls.count(a_ls[i]) == 1:
        rlt[0] = a_ls[i]
    if b_ls.count(b_ls[i]) == 1:
        rlt[1] = b_ls[i]
print(rlt[0], rlt[1])

```
- 15894 수학은 체육과목입니다
```python
n = int(input())
print(4*n)
```
- 9063 대지
```python
n = int(input())
a_ls = []
b_ls = []
for i in range(n):
    a, b = map(int, input().split())
    a_ls.append(a)
    b_ls.append(b)
a_max = max(a_ls)
a_min = min(a_ls)
b_max = max(b_ls)
b_min = min(b_ls)

print((a_max-a_min)*(b_max-b_min))
```

- 10101 삼각형 외우기
```python
a = int(input())
b = int(input())
c = int(input())
if a + b + c != 180:
    print('Error')
elif a == b == c == 60:
    print('Equilateral')
elif a != b and b != c and c != a:
    print('Scalene')
else:
    print('isosceles')
```

- 5073 삼각형의 세 변
```python
T = 1
while T == 1:
    a, b, c = map(int,input().split())
    ls = [a, b, c]
    ls.sort() 
    if a == b == c == 0:
        break
    elif ls[2] - ls[0] - ls[1] >= 0:
        print('Invalid')
    elif a == b == c:
        print('Equilateral')
    elif a != b and b != c and c != a:
        print('Scalene')
    else:
        print('Isosceles')
```

- 14215 세 막대
```python
a = list(input().split())
a.sort()
if a[0] + a[1] - a[2] > 0:
    print(sum(a))
else:
    print(2*(a[0] + a[1]) - 1)
```

### 백준 11단계
- 24262 알고리즘 수업 1
```python
print(1)
print(0)
```
- 24263 알고리즘 수업2
```python
n = int(input())
print(n)
print(1)
```
- 24264 알고리즘 수업3
```python
n = int(input())
print(n**2)
print(2)
```
- 24265 알고리즘 수업4
```python
n = int(input())
num = 0
for i in range(1, n):
    num += i
print(num)
print(2)
```

- 24266 알고리즘 수업5
```python
n = int(input())
print(n**3)
print(3)
```
- 24267 알고리즘 수업6
```python
n = int(input())
num = 0
for i in range(1, n-1):
    num += i * (n - i - 1)
print(num)
print(3)
```

- 24313 알고리즘 수업 - 점근적1
```python
a, b = map(int, input().split())
c = int(input())
n = int(input())
fx = a*n + b
gx = c*n
if b > 0 and gx >= fx:
    print(1)
elif b < 0 and c >= a:
    print(1)
else:
    print(0)
```
### 백준 12단계
- 2798 블랙잭
```python
N, M = map(int, input().split())
ls = list(map(int, input().split()))
rlt = []
for i in range(len(ls)-2):
    for j in range(i+1, len(ls)-1):
        for k in range(j+1, len(ls)):
            if ls[i] + ls[j] + ls[k] <= M:
                rlt.append(int(ls[i] + ls[j] + ls[k]))
print(max(rlt))
```
- 2231 분해합
```python
n = int(input()) 

for i in range(1, n+1):
    num = sum((map(int, str(i))))
    num_sum = i + num  
    
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
```

- 19532 수학은 비대면강의입니다
```python
a, b, c, d, e, f = map(int, input().split())
x = (c*e-b*f)//(a*e-b*d)
y = (c*d-a*f)//(b*d-a*e)
print(x, y)
```