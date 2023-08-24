import sys
sys.stdin = open('input.txt')
bi_list = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
transform = [(2, 1, 1), (2, 2, 1), (1, 2, 2), (4, 1, 1), (1, 3, 2), (2, 3, 1), (1, 1, 4), (3, 1, 2), (2, 1, 3), (1, 1, 2)]
Test = int(input())
for test in range(Test):
    N, M = map(int, input().split())
    raw_data = sorted(list(set([input().strip() for _ in range(N)])), reverse=True)
    raw_data.pop()

    raw_password = ''
    for i in range(len(raw_data)):
        raw_data[i] = raw_data[i].rstrip('0')
        for j in range(len(raw_data[i])):
            word = raw_data[i][j]
            if word.isdigit():
                raw_password += bi_list[int(word)]
            else:
                raw_password += bi_list[ord(word) - 55]
    raw_password.rstrip('0')


    raw_password = raw_password.rstrip('0')
    check_list = []
    ans = 0

    code = []
    length = len(raw_password)
    n1 = n2 = n3 = n4 = 0
    for idx in range(length-1, -1, -1):
        if raw_password[idx] == '1' and not n3:
            n4 += 1
        elif raw_password[idx] == '0' and not n2:
            n3 += 1
        elif raw_password[idx] == '1' and not n1:
            n2 += 1
        elif raw_password[idx] == '0':
            if raw_password[idx-1] == '1':
                n = min(n2, n3, n4)
                code.append(transform.index((n2//n, n3//n, n4//n)))
                n1 = n2 = n3 = n4 = 0
                if len(code) == 8:
                    if code not in check_list:
                        if not ((code[7] + code[5] + code[3] + code[1]) * 3 + code[6] + code[4] + code[2] + code[0]) % 10:
                            ans += sum(code)
                            check_list.append(code[:])
                    code = []

    print(f'#{test+1} {ans}')
