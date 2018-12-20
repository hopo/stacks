# https 사이트 적용하기

### http에 https에 적용한다
+ http는 80포트를 이용, https는 443포트를 이용
+ 보안이 중요하지 않는 path에 한해서 사용하지 않는 경우도 있음
	- 속도가 http가 나아서
+ nginx(apache2) 레이어에서 설정
	- `/etc/nginx/sites-available/` 에 `*.conf`라는 형식의 설정파일이 있음
	- 안전을 위해 `/etc/nginx/sites-enabled/`에 링크 되어 있기도 함
+ 설정파일 안에는 인증서, 암호키, 로케이션 설정 등을 할 수 있음
	- 암호키는 `*.pem`, `*.key` 형태
	- 암호키는 ssl서비스에 따라 자동 갱신되거나 path지정을 해아함


### https 서비스 방법
1. 도메인 구매하듯이 구매를 하여 구매, 설정 후 이용.
	- 비용이 발생
2. AWS 로드밸런스를 이용하여 이용.
	- 관리는 비교적 쉬우나 프론트엔드, 백엔드 서버가 분리 되어 있지 않은 경우 되지 않는 사례가 있음
3. 'Let’s Encrypt'와 같은 서비스 이용.
	- 무료
	- 그러나 지속적인 갱신이 필요함


### 3번 방법인 `Let’s Encrypt`에 대하여
+ 참고 사이트
	- [letsencrypt](https://letsencrypt.org/)
	- [블로그: Let’s Encrypt 를 사용하여 무료로 SSL 사이트를 구축하는 방법](https://blog.lael.be/post/5107)
+ 3개월(90일)마다 갱신을 하여야 한다
	- 방법1
		```
		$ sudo letsencrypt renew`
		$ sudo service nginx restart`
		```
	- 방법2
		```
		certbot renew --post-hook=“service apache2 restart”
		```
+ 3개월마다 갱신을 cron을 이용하여 스케쥴링 관리한다

