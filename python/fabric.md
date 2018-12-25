# deploy 문서
### 출처: junglekim


## \# deploy 환경 설정
1. `mykey.pem` 키 파일을 다운로드 받아 `~/.ssh/mykey.pem`에 옮긴다.
2. `~/.ssh/config` 파일을 열어서 아래 내용을 추가한다.
```
Host dev.myexample.com
    User ubuntu
    IdentityFile ~/.ssh/mykey.pem

Host myexample.com
    User ubuntu
    IdentityFile ~/.ssh/mykey.pem
```
3. `pip3 install fabric3`를 실행해서 fabric을 install 한다.


## \# deploy 방법
서버에 접속해서 손으로 커맨드를 입력하던 기존의 방법을 `Fabric3`를 사용하여 자동화  
deploy 스크립트는 `fabfile.py` 참고


#### deploy 커맨드
** 개발 서버**
`fab dev`

** 프로덕션 서버**
`fab prod`


#### deploy 커맨드 실행 시 순서
1. 자신의 local 프로젝트의 branch 이름과 commit hash를 가져온다.
2. local에서 얻은 branch 이름과 commit hash를 통해 서버의 코드를 업데이트한다.
	- 예를 들어, local branch가 `dev`였다면, 서버의 branch도 `dev`로 설정된다.
3. 패키지를 인스톨한다.
4. Static 파일을 업데이트한다.
	- javascript, css, img 등 `static` 폴더 하위의 파일들
5. 데이터베이스를 업데이트한다.
6. uwsgi 서버를 재실행한다.


#### 주의사항
- deploy는 커맨드를 입력한 사람의 local을 branch와 commit hash를 기준으로 한다.
- deploy 할 branch와 commit은 반드시 Github에 push되어 있어야 한다.
- 개발의 경우 branch 제한없이 deploy할 수 있다.
- 프로덕션의 경우 master branch만 deploy 할 수 있다.


---
## \# 참고
- [branch 관리 가이드](https://guides.github.com/introduction/flow/)
