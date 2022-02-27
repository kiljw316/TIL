# Spring Framework의 개요(정의와 전략)

## Spring Framework란?

Java 엔터프라이즈 개발을 편하게 해주는 오픈소스 `경량급 애플리케이션 프레임워크`이다.

애플리케이션 프레임워크

- 특정 계층이나 기술, 업무분야에 국한되지 않고 애플리케이션의 전 영역을 포괄하는 범용적인 프레임워크를 말한다.

경량급 프레임워크

- 단순한 웹컨테이너에서도 엔터프라이즈 개발의 고급기술을 대부분 사용할 수 있다.

엔터프라이즈 개발 용이

- 개발자가 복잡하고 실수하기 쉬운 Low Level(보안, 인증, 트랜잭션 처리 등)에 많이 신경 쓰지 않으면서 Business Logic 개발에 전념할 수 있도록 해준다.

오픈소스

- Spring은 OpenSource의 장점을 충분히 취하면서 동시에 OpenSource 제품의 단점과 한계(==오픈 소스의 장점과 꾸준한 지원)를 잘 극복한다.

## Spring Framework 전략

Spring 삼각형

엔터프라이즈 개발의 복잡함을 상대하는 Spring의 전략
-> `Portable Service Abstraction, DI, AOP, POJO`

- Portable Service Abstraction(서비스 추상화)

  - 트랜잭션 추상화, OXM(Object XML Mapping) 추상화, 데이터 액세스의 Exception 변환기능 등 기술적인 복잡함은 추상화를 통해 Low Level의 기술 구현 부분과 기술을 사용하는 인터페이스로 분리한다.

- 객체지향과 DI(Dependency Injection)

  - Spring은 객체지향에 충실한 설계가 가능하도록 단순한 객체 형태로 개발할 수 있고, DI 는 유연하게 확장 가능한 객체를 만들어 두고 그 관계는 외부에서 다이내믹하게 설정해준다.

- AOP(Aspect Oriented Programming)

  - AOP는 애플리케이션 로직을 담당하는 코드에 남아 있는 기술 관련 코드를 분리해서 별도의 모듈로 관리하게 해주는 강력한 기술이다.

- POJO(Plain Old Java object)

  - POJO는 객체지향 원리에 충실하면서, 특정 환경이나 규약에 종속되지 않고 필요에 따라 재활용될 수 있는 방식으로 설계된 객체이다.
  - JVM만 있다면 동작하는 자바 객체를 POJO라고 볼 수 있다.

# Spring framework의 특징

## Spring Framework 특징

1. `컨테이너 역할`

- Spring 컨테이너는 Java 객체의 LifeCycle을 관리하며, Spring 컨테이너로 부터 필요한 객체를 가져와 사용할 수 있다.

2. `DI(Dependency Injection) 지원`

- Spring은 설정 파일(XML)이나 어노테이션(Component)을 통해서 객체 간의 의존관계를 설정할 수 있도록 하고 있다.

3. `AOP(Aspect Oriented Programming) 지원`

- Spring은 트랜잭션이나 로깅, 보안과 같이 공통적으로 필요로 하는 모듈들을 실제 핵심 모듈에서 분리해서 적용할 수 있다.

4. `POJO(Plain Old Java Object) 지원`

- Spring 컨테이너에 저장되는 Java객체는 특정한 인터페이스를 구현하거나, 특정 클래스를 상속받지 않아도 된다.

5. `트랜잭션 처리를 위한 일관된 방법을 지원`

- JDBC, JTA 등 어떤 트랜잭션을 사용하던 설정(XML, annotation 등)을 통해 정보를 관리하므로 트랜잭션 구현에 상관없이 동일한 코드 사용가능

6. `영속성(Persistence)과 관련된 다양한 API 지원`

- Spring은 MyBatis, Hibernate 등 데이터베이스 처리를 위한 ORM(Object Relational Mapping) 프레임워크들과의 연동 지원

# Spring Framework의 기능요소

## Spring 프레임워크를 구성하는 기능 요소

1. Spring Core(Core 컨테이너)

- Spring프레임워크의 기본기능을 제공한다.
- 이 모듈에 있는 BeanFactory는 Spring의 기본 컨테이너이면서 스프링 DI의 기반이다.

2. Spring AOP

- 업무 로직과 공통로직 분리가 AOP
- AOP 모듈을 통해 Aspect 지향 프로그래밍을 지원한다.
- AOP모듈은 스프링 애플리케이션에서 Aspect를 개발할 수 있는 기반을 지원한다.

3. Spring ORM

- MyBatis, Hibernate, JPA 등 널리 사용되는 ORM 프레임워크와의 연결고리를 제공한다.
- ORM 제품들을 Spring의 기능과 조합해서 사용할 수 있도록 해준다.

4. Spring DAO

- JDBC에 대한 추상화 계층으로 JDBC 코딩이나 예외처리 하는 부분을 간편화 시켰으며, AOP 모듈을 이용해 트랜잭션 관리 서비스도 제공한다.

5. Spring Web

- 일반적인 웹애플리케이션 개발에 필요한 기본기능을 제공한다.
- Webwork나 Struts와 같은 다른 웹애플리케이션 프레임워크와의 통합을 지원한다.

6. Spring Context

- Context 모듈은 BeanFactory의 개념을 확장한 것으로 국제화(I18N) 메시지, 애플리케이션 생명주기 이벤트, 유효성 검증 등을 지원한다.

7. Spring Web MVC(Model/View/Controller)

- 사용자 인터페이스가 애플리케이션 로직과 분리되는 웹 애플리케이션을 만드는 경우에 일반적으로 사용되는 패러다임이다.

# 학습 정리

Spring Framework 정의

- Java 엔터프라이즈 개발을 편하게 해주는 오픈소스 경량급 애플리케이션 프레임워크이다.

Spring Framework 전략

- Portable Service Abstraction, DI, AOP, POJO

Spring Framework 특징

- 컨테이너, DI와 AOP,POJO 지원, 일관된 트랜잭션 처리방법, 다양한 ORM과의 연동

Spring Framework 기능요소

- Core 컨테이너, Context, DAO, ORM, AOP, Web, WebMVC
