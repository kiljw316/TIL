# http와 https의 차이점은 무엇인가

## http의 약점
* 암호화가 되지 않은 평문 데이터를 전송하기 때문에 도청가능
* 통신 상대를 확인하지 않기 때문에 위조, 변조 가능

## 통신 암호화
http에는 암호화 구조가 없지만, SSL(Secure Socket Layer)이나 TLS(Transport Layer Security)라는 프로토콜을 조합함으로써 http의 통신 내용을 암호화할 수 있음

ssl을 조합한 http를 https 라고 부름

## 상대를 확인하는 증명서
* http에서는 통신 상대를 확인할 수 없다. => ssl로 상대를 확인할 수 있음
* 상대를 확인하는 수단으로 증명서를 제공
* 증명서는 신뢰할 수 있는 제 3가 기관에 의해 발행
* 증명서 위조는 기술적으로 상당히 어려움

## https는 ssl의 껍질을 덮어쓴 http
* https는 새로운 애플리케이션 계층의 프로토콜이 아님
* http통신을 하는 소켓 부분을 ssl이나 tls 라는 프로토콜로 대체하고 있을 뿐

## 왜 항상 https를 사용하지 않을까?
* https는 안전하게 데이터를 주고받을 수 있지만 https를 이용하면 암호화/복호화의 과정이 필요하기 때문에 http보다 속도가 느리다(최근에는 거의 차이를 못 느낌).
* https는 인정서를 발급하고 유지하기 위한 추가 비용이 발생

## https의 개념
* http에 데이터 암호화가 추가된 프로토콜
* https는 http와 다르게 443번 포트를 사용, 네트워크 상에서 중간에 제3자가 정보를 볼 수 없도록 공개키 암호화를 지원

## 공개키/개인키
https는 공개키/개인키 암호화 방식을 이용해 데이터를 암호화하고 있으며 공개키와 개인키는 서로를 위한 1쌍의 키이다
* 공개키: 모두에게 공개가능한 키
* 개인키: 나만 가지고 알고 있어야 하는 키

## 공개키/개인키 암호화의 효과
* 공개키 암호화: 공개키로 암호화를 하면 개인키로만 복호화할 수 있다. => 개인키는 나만 가지고 있으므로, 나만 볼 수 있다.

* 개인키 암호화: 개인키로 암호화하면 공개키로만 복호화할 수 있다. => 공개키는 모두에게 공개되어 있으므로 내가 인증한 정보임을 알려 신뢰성을 보장할 수 있다.

## SEO를 개선하는 SSL
* 2014년 Google은 웹 전역의 보안을 개선하기 위해 모든 영역에서 HTTPS를 사용할 것을 요청했으며 높은 순위의 SSL 보안 사이트에 보상을 제공했습니다. 

* 2018년, Google은 단순한 검색 엔진을 넘어, Chrome 브라우저에서 SSL 인증서가 포함되저 있지 않은 사이트를 "안전하지 않음"이라고 표시하는 방식으로 처벌했습니다.

## 정리
* 개인 정보와 같은 민감한 데이터를 주고 받아야 한다면 HTTPS를 이용해야 하지만, 단순한 정보 조회 등만을 처리하고 있다면 HTTP를 이용하면 되겠다.

 
## HTTPS의 보안 작동 방식
* 만일, 클라이언트(웹브라우저)가 평범한 http가 아닌 https 스킴을 갖는 URL 주소를 만나면,
     - 웹서버에 80번이 아닌 443번 포트번호로 `TCP 연결`을 맺고,
     - 바이너리 포멧으로 된 몇몇 보안 매개변수를 교환(핸드세이크, `키 교환`)하고,
     - 그와 관련된 HTTPS 명령들이 그 뒤를 잇게 됨 


## 단순하게 https를 사용한다고 해서 보안이 더 나아지는가
* http는 데이터 자체가 변조되거나 탈취당할 수 있지만 
* https는 암호화 키를 먼저 가로채 가야하는 과정이 생기기 때문에 https로 통신하는 것이 보안에 더 나음

## Q2 RTC는 왜 https 상에서만 작동하는가
chrome37버젼이상부터 http로는 미디어스트림을 얻을 수 없음(getUsermedia)
getUsermedia를 사용하는 클라이언트가 https가 아니면 사용 불가

## 출처
* http와 https의 차이 [https://antstudy.tistory.com/250](https://antstudy.tistory.com/250)
* http와 https의 특징과 차이 [https://yuricoding.tistory.com/82](https://yuricoding.tistory.com/82)
* 다니의 HTTPs [https://www.youtube.com/watch?v=wPdH7lJ8jf0&list=TLPQMjIwMTIwMjJm5RC6ZoYp7A&index=2](https://www.youtube.com/watch?v=wPdH7lJ8jf0&list=TLPQMjIwMTIwMjJm5RC6ZoYp7A&index=2)