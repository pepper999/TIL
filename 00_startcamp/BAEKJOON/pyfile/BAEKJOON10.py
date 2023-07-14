# 27323 직사각형

# A = int(input())
# B = int(input())

# print(A*B)

# 직사각형에서 탈출

# x, y, w, h = map(int, input().split())

# a, b = 0, 0

# if x > w-x:
#     a = w-x
# else:
#     a = x
# if y > h-y:
#     b = h-y
# else:
#     b = y

# if a > b:
#     print(b)
# else:
#     print(a)

# 3009 네 번째 점

# a_ls = []
# b_ls = []
# rlt = [0,0]
# for i in range(3):
#     a, b = map(int, input().split())
#     a_ls.append(a)
#     b_ls.append(b)

# for i in range(3):
#     if a_ls.count(a_ls[i]) == 1:
#         rlt[0] = a_ls[i]
#     if b_ls.count(b_ls[i]) == 1:
#         rlt[1] = b_ls[i]
# print(rlt[0], rlt[1])

# 15894 수학은 체육과목입니다
# n = int(input())
# print(4*n)

# 9063 대지

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