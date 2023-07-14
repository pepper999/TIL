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