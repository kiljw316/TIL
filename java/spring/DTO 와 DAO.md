# DAO(Data Access Object)

- DB를 사용해서 데이터를 조작하는 기능(CRUD)을 전담하도록 만든 오브젝트이다.

- DB 접근을 위한 로직과 비즈니스 로직을 분리하기 위해 사용된다. 자신이 필요한 Interface를 DAO에 전달하고, DAO는 인터페이스를 구현한 객체를 가공해 사용자에게 반환한다.
- DAO는 어떤 DB, Drive, 계정으로 접근할지 설정하고 작업을 진행하여 처리된 결과를 반환한다.
- DB에 대한 접근을 DAO가 하게된다면 다수의 원격 호출을 통한 오버헤드를 VO나 DTO를 통해 줄일 수 있고, 다수의 DB 호출문제를 해결할 수 있다.
- DAO가 제공하는 오퍼레이션이 Repository가 제공하는 오퍼레이션보다 더 세밀하다.

# DTO(Data Transfer object)

- 계층 간 데이터 교환을 위한 객체(Java Beans)이다.

- 폼 필드의 이름을 그대로 가지고 있는 자바빈 객체를 폼 필드와 그대로 매핑하여 비즈니스 계층으로 보낼 때 사용된다.
- DTO는 로직을 가지고 있지 않는 순수한 데이터 객체이며, 속성과 그 속성에 접근하기 위한 Getter / Setter 메소드만을 갖는다.

# VO(Value Object)

- Read-Only 속성을 띄는 값 Object 이다.

- 핵심 역할은 equals() 와 hashcode()를 오버라이딩 하는 것이다.
- VO는 테이블 내의 속성 외에도 추가적인 속성을 가질 수 있으며, 여러 테이블의 공통 속성을 모아 만든 베이스를 상속받아 사용할 수도 있다.
- VO는 특정한 비즈니스 값을 담는다면, DTO는 계층 간의 데이터 이동을 위해 사용된다.
