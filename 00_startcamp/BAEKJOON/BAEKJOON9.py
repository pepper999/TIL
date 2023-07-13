# 5086 배수
# num1, num2 = 2, 2
# while num1 != 0 and num2 != 0:
#     num1, num2 = map(int, input().split())

#     if num1 > num2 and num1%num2 == 0:
#         print('multiple')
#     elif num1 < num2 and num2%num2 == 0:
#         print('factor')
#     elif num1 != 0 and num2 != 0:
#         print('neither')
#     else:
#       break

# 2501 약수 구하기
# N, K = map(int, input().split())
# ls = [0]*N
# for i in range(1, N+1):
#     if N%i == 0 :
#         ls[i-1] = i
# for i in range(len(ls)):
#     try:
#         ls.remove(0)
#     except:
#         break

# try:
#     print(ls[K-1])
# except:
#     print(0)

# 9506 약수들의 합
# n = 0
# ls = [6, 28, 496, 8128, 33550336]
# while n != -1:
#     ls2 = []
#     prints = []
#     n = int(input())
#     if n in ls:
#         for i in range(1, n+1):
#             if n%i == 0:
#                 ls2.append(i)
#         print(n,'=', end = ' ')
#         for j in range(len(ls2)):
#             prints.append(ls2[j])
#             prints.append('+')
#         for j in range(len(prints)-3):
#             print(prints[j], end = ' ')
#         print()
#     elif n == -1:
#         break
#     else:
#         print(n, 'is NOT perfect.')

# 1978 소수 찾기

n = int(input())
num = list(map(int, input().split()))
rlt = 0
for i in range(n):
    for j in range(2, num[i]):
        if num[i]%j == 0:
            break
        else:
            pass
        
print(rlt)   
