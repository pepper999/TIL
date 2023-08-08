import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(T):
    str_dict = dict()
    str1 = input()
    for i in range(len(str1)):
        str_dict[str1[i]] = 0
    str2 = input()
    for i in range(len(str2)):
        if str_dict.get(str2[i]) != None:
            str_dict[str2[i]] += 1
    print(f'#{t+1}', max(str_dict.values()))