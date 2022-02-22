# 스프링 프레임워크의 특징 및 장점

> 객체지향 프로그래밍(OOP)에 기반

- 서버 개발 시 크게 3계층으로 나누어 구현 가능 (Controller, Service, Repository)
- 클래스 1개를 선언하여 재사용 가능
- 모듈화가 잘 되어 있어, 필요한 모듈들만 레고처럼 조립하여 사용 가능

  - 스프링 시큐리티
  - 스프링 타임리프

<br>

> DI(의존성 주입) 지원

- DI를 통해 강한 결합의 문제점을 해결

<br>

> 비즈니스 로직에 집중 가능

- 웹 서버에서는 비즈니스 로직이 가장 중요한 구현 부분

- 비즈니스 로직 외에 다른 부분은 스프링 프레임워크가 쉽게 구현 가능하도록 도움을 줌
  - `Client` 와의 `communication` 역할을 하는 `Controller`
  - `DB`와의 `communication` 역할을 하는 `Spring Data JPA`

<br>

> 그 외

- AOP 지원

- 테스트 코드 작성이 수월함
- 20여년 동안 발전한 프레임워크

  - 개발 편의성이 계속 나아짐
  - 많은 기업에서 사용하며 입증된 신뢰성