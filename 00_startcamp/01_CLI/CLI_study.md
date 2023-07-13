# CLI

- Command_line_interface

- 새 폴더 만들기
```bash
$ mkdir new_folder
```

- 작업 위치를 new_folder로 이동
```bash
$ cd new_folder
```

- 현재 작업 위치를 열기
```bash
# . -> 상대 경로 상의 현재 위치
$ start .
```

- 현재 폴더를 vscode로 열기
```bash
$ code .
```

- 없는 파일은 새파일 생성, 있는 파일은 파일을 엶
```bash
$ code README.md
```

- 현재 위치의 파일 목록 불러오기
```bash
$ ls
```

- 파일의 이름을 바꾸거나 위치를 옮긴다
```bash
$ mv {이동할 대상}{이동할 위치}
$ mv {이름 바꿀 대상}{바꿀 이름}
```

### 상대 경로 절대 경로
1. 절대경로 : 모든 경로를 표시한 것(/c/Isers/SSAFY/~)
2. 상대경로 : 나를 기준으로 경로를 지정(현재 위치, 상위폴더..)
3. 삭제
```bash
$ rm {파일명}
$ rm -r {폴더}
```
- '-{약어}','--{풀 네임}', -r(재귀)
- 파일삭제시 조심!!!

### AI
- ChatGPT 생성모델/ 사전훈련/ 트랜스포머 AI 모델
- 마소 오픈형 AI 지원, 깃헙 운영, 깃헙 코드로 훈련
- ChatGPT 사용시 추가 조건 사용 가능(노션 참고)

### API
- ex) 라이엇이 게임 API를 제공해서 op.gg를 통해 사용자 정보를 볼 수 있음
1. 응답 데이터에서 응답 메세지를 가져온다.
respone = res.data.choices[0].message.content
주석 해제하려는 영역 드래그 후, 'Ctrl + /'
    - 클라이언트 문제 4XX
    - 서버 문제 5XX
    - 성공 시 2XX