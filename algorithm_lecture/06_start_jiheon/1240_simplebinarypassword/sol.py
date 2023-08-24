bi_dict = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9}
Test = int(input())
for test in range(Test):
    maybe_password = set()
    N, M = map(int, input().split())
    for _ in range(N):
        password = input()
        if '1' in password:
            maybe_password.add(password)
    password = list(maybe_password)[0]
    length = len(password) - 1  # 마지막 인덱스
    where = 0
    for idx in range(length, 0, -1):
        if password[idx] == '1':
            where = idx - 55
            break
    ans_list = []
    for i in range(8):
        ans_list.append(bi_dict[password[where + 7 * i:where + 7 * (i + 1)]])
    check = 0
    for i in range(8):
        if i % 2:
            check += ans_list[i]
        else:
            check += ans_list[i] * 3
    if check % 10:
        print(f'#{test + 1} 0')
    else:
        print(f'#{test + 1} {sum(ans_list)}')