# WebSocket
>양방향 소통을 위한 프로토콜

## webSocket 주요 기능
- HTML5 웹 표준 기술

- 정확성과 효율성
- 실시간 커뮤니케이션
- 매우 빠르게 작동하며 통신할 때 아주 적은 데이터를 이용함
- 이벤트를 단순히 듣고 보내는 것만 가능
- 한쪽에서 연결을 종료할 때까지 유지

<br>
<br>

# Socket.IO
>양방향 통신을 하기위해 웹소켓 기술을 활용하는 라이브러리

## Socket.IO 주요 기능
- 표준 기술이 아니며, 라이브러리임

- 모든 플랫폼에서 작동
- 소켓 연결 실패 시 fallback을 통해 다른 방식으로 스스로 해당 클라이언트와 연결을 시도함
- room, namespace 개념을 이용해 일부 클라이언트에게만 데이터를 전송하는 브로드캐스팅이 가능함

<br>
<br>

# 비교
|no|웹소켓|Socket.IO|
|--|------|--------|
|1|tcp 연결을 통해 설정되는 프로토콜|웹소켓과 함께 작동하는 라이브러리|
|2|전이중 통신 제공|브라우저와 서버 간의 이벤트 기반 통신|
|3|브로드캐스트 미지원|브로드캐스트 지원|
|4|fallback 옵션 없음|fallback 옵션 있음|

<br>
<br>

# 적합한 사용 방법

* WebSocket: 주식 거래소 같이 실시간 데이터 전송이 많은 경우에는 빠르고 비용이 적은 표준 WebSocket을 사용

* Socket.IO: 사용자들을 room, namespace로 나눠서 브로드 캐스팅이 필요한 경우 사용


<br>
<br>


## 출처

- [https://www.peterkimzz.com/websocket-vs-socket-io/ - 웹소켓과 socket.io ](https://www.peterkimzz.com/websocket-vs-socket-io/)
- [https://www.educba.com/websocket-vs-socket-io/ - educa](https://www.educba.com/websocket-vs-socket-io/)
