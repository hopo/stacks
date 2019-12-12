### nginx 504 접속 불가 & ssh 접속불가와 같은 상황

#### 복구를 위한 작업자의 행동 (-> 서버컴퓨터 reboot & set)
1. aws-ec2 instance를 reboot
  + ec2 instance stop & start
  + 유동ip 사용 하는 경우, 변경된 public ip를 확인

2. ssh로 서버컴퓨터 접속
  + ip가 변경되었다면 nginx 설정 변경
    - /etc/nginx/site-available/
    - 기존 conf 파일을 백업
    - conf 파일에 들어가 server_name의 ip를 변경 (hosts 관련)
  + service nginx stop & start
    - 정상 작동이 되지 않는다면 log를 잘 살펴가며..

4. aws-route53에서 도메인 주소 setting
  + 도메인, ip, dns등의 setting이 잘되었는지 확인  

5. code deploy
