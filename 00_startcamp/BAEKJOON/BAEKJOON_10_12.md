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