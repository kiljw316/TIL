WebRTC 용어 정리

1. Signaling 서버(P2P, Mesh) 방식: 서버에게 시그널을 보내 서로의 정보를 확인하고 직접 통신
2. SFU(Selective Forwarding Unit) 서버 방식: 종단 간 미디어 트래픽을 중계하는 중앙 서버 방식
3. MCU(Multi-point Control Unit) 서버 방식: 다수의 송출 미디어를 중앙 서버에서 혼합하여 수신측으로 전달하는 중앙 서버 방식

ICE(Interactive Connectivity Establishment)

- 브라우저가 peer를 통한 연결이 가능하도록 해주는 프레임 워크

STUN(Session Traversal Utilities for NAT) 서버

- 클라이언트 자신의 Public Address(IP:PORT)를 알려준다.

NAT(Network Address Translation)

- 단말에 공개 IP(Public IP) 주소를 할당하기 위해 사용한다.

Symmetric NAT

- 패킷을 보내는 외부 서버마다 다른 NAT 매핑을 사용한다. PC에서 패킷을 특정 서버로 보내면 그 서버에서 보낸 패킷만 PC로 전달된다.
클라이언트와 서버 통신 시 둘중 하나라도 Symmetric NAT이 아니라면 괜찮지만 둘 다 라면 서로의 요청과 응답을 못 받을 수 있음


TURN(Traversal(순회) Using Relays around NAT) 서버

- TURN 서버와 연결하고 모든 정보를 그 서버에 전달하는 것으로 Symmetric NAT 제한을 우회하는 것을 의미한다.

MediaStream(getUserMedia)

- 사용자의 카메라와 마이크 같은 곳의 데이터 스트림에 접근한다.

RTCPeerConnection

- 암호화 및 대역폭 관리를 하는 기능을 가지고 있고, 오디오 또는 비디오 연결을 한다.

Data Channel

- offer 하는 socket이 데이터 채널을 생성하는 주체가 되어야 함
