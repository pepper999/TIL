# 27323 직사각형

# A = int(input())
# B = int(input())

# print(A*B)

# 직사각형에서 탈출

x, y, w, h = map(int, input().split())

a, b = 0, 0

if x > w-x:
    a = w-x
else:
    a = x
if y > h-y:
    b = h-y
else:
    b = y

if a > b:
    print(b)
else:
    print(a)

