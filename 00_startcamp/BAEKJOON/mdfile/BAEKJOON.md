# 백준 문제풀이
### 기타
- 1076 저항
```python
ls1 = ['balck', 'brown','red','orange','yellow','green','blue','violet','grey','white']
ls2 = [10**i for i in range(len(ls1))]

A = str(input())
B = str(input())
C = str(input())

print(str(ls1.index(A)) + str(ls1.index(B)))
```
