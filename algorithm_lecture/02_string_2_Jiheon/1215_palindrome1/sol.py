T = 10
for tc in range(1, T+1):

    # palindrome 의 길이 입력
    p = int(input())
    # 평면 글자판은 8x8
    N = 8
    # 글자판 입력
    arr = [list(input()) for _ in range(N)]

    # 회문의 수를 구하기 위해 변수 초기화
    cnt = 0

    # 가로일 때
    for i in range(0, N):
        for j in range(0, N-p+1):
            # 글자판 i번째 행의 j번째 열부터 회문의 길이만큼의 문장과 그 역순 문장이 같으면
            if arr[i][j:j+p] == arr[i][j:j+p][::-1]:
                # 회문이므로, cnt에 1을 더해준다.
                cnt += 1

    # 세로일 때
    for j in range(0, N):
        for i in range(0, N-p+1):
            # 세로 문장을 확인하기 위해 char 변수 생성 및 초기화
            char = ''
            # i번째 행부터 회문의 길이만큼 문자열을 char 변수에 저장
            for ci in range(i, i+p):
                char += arr[ci][j]
            # char 문장과 그 역순 문장이 같으면 회문이므로, cnt에 1을 더해준다.
            if char == char[::-1]:
                cnt += 1

    # 결과 출력
    print('#{} {}'.format(tc, cnt))
    
