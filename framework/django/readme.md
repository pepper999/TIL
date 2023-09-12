# 시작하기 전에

## 프로젝트 관리
- TIL, 학습하고 있는 각종 폴더, 관통 PJT
- git 으로 관리
- .gitignore 만드셈~ -> 가상환경 떄문에(git 으로 관리 X)

## 가상 환경
- 분리해서 관리해야 하니까
- git 으로 관리 X
- requirements.txt -> 해당 프로젝트를 위한 독립 환경 목록

### 가상환경 생성
```bash
# 작업위치 확인하기
$ python -m venv { folder_name}
```

### 가상환경 실행
```bash
$ ls { venv folder_name }/
$ source { folder_name }/Scripts/Activate

( folder_name )
$ pip list
```

### 다른 작업 환경을 위한 설정
```bash
# 현재 pip 목록을 얼린다.
$ pip freeze > requirements.txt

# requirements.txt 파일에 적힌 내용으로 설치
$ pip install -r requirements.txt
```

## Django 프로젝트 생성
```bash
# Django 프로젝트 생성
# offline 이름의 프로젝트
$ django-admin startproject offline
$ cd offline

# 현재 작업 위치에 프로젝트 생성
$ django-admin startproject offline .
```

### Django 서버 실행
```bash
$ python manage.py runserver
```

### Django App 추가하기
```bash
$ python manage.py startapp articles
```
```python
# settings.py의 INSTALLED_APPS에 app 추가하기
INSTALLED_APPS = ['app name']
```

### articles app의 메인 페이지 화면에 띄우기
1. client가 요청 보낼 경로 지정하기 -> url
2. 특정 경로에 요청이 왔을떄, 그 요청에 적절한 처리 하기 -> views.py
3. 적절한 처리 과정에서 template(html)이 필요하다면, 작성하기 -> templats/*.html
4. 작정된 template을 사용자에게 반환하기 -> views에 정의한 함수의 return