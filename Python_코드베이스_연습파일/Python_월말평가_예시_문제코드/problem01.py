# 파이썬 내장함수 min 사용 금지
def min_score(scores):
    min_scre = scores[0]
    for i in range(len(scores)-1):
        if min_scre > scores[i+1]:
            min_scre = scores[i+1]
    return min_scre
    # 여기에 코드를 작성합니다.


if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    scores = [30, 60, 90, 70]
    print(min_score(scores)) # 30
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    
