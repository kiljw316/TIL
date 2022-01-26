# 웹소켓이 아닌 소켓io를 선택한 이유

이미지 예시 - 사진 밑에 출처도 표기해주세요!

<img src="https://t1.daumcdn.net/cfile/tistory/2513B73B577F20AE3C">

[이미지 출처](https://t1.daumcdn.net/cfile/tistory/2513B73B577F20AE3C)

- 피어들의 시그널링 작업을 위해 소켓 통신(양방향 통신)을 선택
- 그 중 기존 tcp/ip 소켓 방식은 서버와 연결되어 있는 모든 포트에 데이터를 전송함
- 하지만 bbomomo 서비스는 room 마다 보내주어야 데이터가 다름

- 사용자들을 room 으로 나눠서 브로드 캐스팅해줄 수 있는 기능이 필요하기 때문에 room과  namespace로 브로드 캐스팅할 수 있는 웹 소켓 방식을 선택
- 웹 소켓의 개발 편의를 위해 웹소켓 프레임워크인 Socket.IO를 사용하기로 함

이미지 예시 - 사진 밑에 출처도 표기해주세요!

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR82yk7rCYhlKHnpb9cGi8PzA4HK5e3X3d3-A&usqp=CAU">

[이미지 출처](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR82yk7rCYhlKHnpb9cGi8PzA4HK5e3X3d3-A&usqp=CAU)

<br>
<br>
<br>
<br>

# RTC는 왜 https 상에서만 작동하는가?

로컬환경에서 webRTC가 정상 작동되는 것을 확인하고 aws ec2 인스턴스에 배포하고 테스트를 해봤지만 Mixed Content Block 에러가 발생해서 찾아보니

이미지 예시 - 사진 밑에 출처도 표기해주세요!
<img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/3QrW4ClgkSb1lNdKysdjto/81977f91736a801e8d892a2406d0f92d/Screen_Shot_2019-01-14_at_4.53.45_PM.png">

[이미지 출처](https://cf-assets.www.cloudflare.com/slt3lc6tev37/3QrW4ClgkSb1lNdKysdjto/81977f91736a801e8d892a2406d0f92d/Screen_Shot_2019-01-14_at_4.53.45_PM.png)

chrome37버젼이상부터 http로는 미디어스트림(getUsermedia)을 얻을 수가 없다고 한다.
getUsermedia를 사용하는 클라이언트가 https가 아니면 사용이 불가능하기 때문에
인증서를 발급받아 https 설정을 했다.

# SFU 와 P2P 중 P2P 방식 선택 이유

단순 스트림 데이터를 받는 것이 아닌 서로의 스트림 데이터를 전송해야되기 때문에
SFU 방식은 서버와 연결된 peer 들의 수가 증가할 수록 높은 성능의 서버를 요구함

낮은 성능의 서버를 이용하는 대신 P2P 방식을 채택하여 서버의 부하는 줄이고 클라이언트에 일부 부담 전가

peer가 증가함에 따른 효율성과 과부하를 고려해서 최대 6인까지만 peer 연결 허용(컴퓨터 사양이 낮은 사용자를 위해 4인까지 줄이는 것도 고려중)
