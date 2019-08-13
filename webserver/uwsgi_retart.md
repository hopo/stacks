### uwsgi 재시작 하기

#### \# 상황

```
run: pip3 -r requirements.txt
```
에서 멈춰 다음 명령어가 먹히지 않는 상황이다.
간혹 느려지거나, ssh 접속으로 컨트롤 하는 것이 제어가 되지 않을 때가 있다.

#### \# 해결방안
시스템에 접속하여

```
# pkill -f uwsgi -9
# uwsgi --ini uwsgi_dev.ini
```

그래도 안된다면 재접속 또는 다음 명령어
```
# service uwsgi status
# service uwsgi stop
# service uwsgi start
```
