# GIT 이란...
> 분산 버전 관리 시스템
    - 코드의 버전을 관리
    - 개발되어 온 과정 파악
    - 이전 버전과의 변경 사항 비교
## Git 의 3가지 영역
1. Working Directory
    - 실제 작업 영역
2. Staging Area
    - Working Directory에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 중간 준비 영역
3. Repository
    - 버전 이력과 파일들이 영구적으로 저장되는 영역 모든 버전과 변경 이력이 기록됨

### Git 초기화
```bash
$ git init
```

### 상태 확인 명령어
```bash
$ git status
```

### staging area에 추가
```bash
$ git add {path}<folder_name>/{file_name}
```

### Repository에 저장하기
```bash
$ git commit -m "commit message"
```

### git 기초 설정
```bash
$ git config --global user.email "hun01414@naver.com"
$ git config --global user.name "정지헌"

$ git config --global --list
```

### 커밋 기록 확인하기
```bash
$ git log
```

### 직전 커밋 수정하기
```bash
$ git commit --amend
# vlm에서 커밋 내용 수정하기
# insert 삽입 상태 -> 메시지 수정 -> esc 삽입 상태 종료 -> :wq로 저장 종료
```

### git 설정 초기화
```bash
# vim을 활용해서 설정 제거하기
# vim git 설정 파일 열기
$ vim ~/.gitconfig
$ code ~/.gitconfig
# insert 키 -> 수정상태 만들기 -> 수정 후 esc로 수정상태 종료 -> :wq로 저장 종료
```
