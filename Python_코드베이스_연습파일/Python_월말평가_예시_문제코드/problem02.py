def under_60(scores):
    cnt = 0
    for i in range(len(scores)):
        if scores[i] < 60:
            cnt += 1
    return cnt
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(under_60(scores)) # 1
    # 아래 부터 추가 예제 코드 작성 가능합니다.

