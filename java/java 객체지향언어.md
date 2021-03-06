# 객체지향언어

Java는 객체지향언어로써 코드간에 관계를 맺어 줌으로써 보다 유기적인 프로그램을 구성할 수 있다.

## 클래스

- 클래스는 표현하고자 하는 대상의 공통 속성을 한 군데에 정의해 놓은 것이라고 할 수 있다.
- 즉, 클래스는 객체의 속성을 정의해 놓은 것이다.
- 클래스 내부의 정보를 멤버 변수라고 한다.

## 인스턴스

- 클래스로부터 만들어진 객체를 그 클래스의 인스턴스라고 한다.
- 인스턴스의 멤버변수에 접근할 때는 `[생성된 인스턴스.멤버변수]`의 형식을 사용한다.

## 메소드

- 메소드는 어떠한 작업을 수행하는 코드를 하나로 묶어 놓은 것이다.

### 메소드가 필요한 이유

1. 재사용성
   - 메소드를 만들어 놓으면 이후 반복적으로 재사용이 가능
2. 중복된 코드 제거
   - 프로그램을 작성하다보면 같은 코드가 여러번 반복되어 작성되곤 하는데, 메소드를 활용하면 중복된 부분을 없애므로 보다 효율적인 코드가 된다.
3. 프로그램 구조화
   - 코드가 작업하는 내용에 따라 구분되어 구조화시킬 수 있다.
   - 메소드 생성 시 메소드 안에서 동작하는 내용을 잘 표현할 수 있도록 이름을 잘 지어주면, 메소드 안을 들여다 보지 않고도 한 눈에 코드를 읽어내려갈 수 있다(가독성이 좋다고 표현함).
     - 동사로 시작
     - camel case로 작성

### 메소드 선언과 구현

```java
메소드 정의

반환타입 메소드이름 (타입 변수명, 타입 변수명, ...) {
    수행되어야 할 코드
}

- 메소드는 return문을 통해 수행의 결과를 반환
- 이때 결과의 자료형을 결정하는 부분이 반환타입

```

## 상속

상속이란 기존의 클래스를 재사용하는 방식 중의 하나이다. 한 번 작성한 코드가 재사용이 필요하다면, 변경사항만 코드로 작성하므로 상대적으로 적은 양의 코드를 작성할 수 있게 된다. 이렇게 코드를 재사용하면, 코드와 클래스가 많아질수록 관리가 용이하다는 장점이 있다.

상속을 통해 클래스간의 계층구조를 만들 수 있다.

상속의 특징

- 부모 클래스에서 정의된 필드와 메소드를 물려 받는다.
- 새로운 필드와 메소드를 추가할 수 있다.
- 부모 클래스에서 물려받은 메소드를 수정할 수 있다.

### 상속의 형식

```java
class Animal{}  // 부모 클래스, 조상 클래스
class Dog extends Animal{}  // 자식 클래스, 자손 클래스
class Cat extends Animal{}  // 자식 클래스, 자손 클래스
```

자식 객체는 자식 타입으로 선언된 변수에도 할당할 수 있고, 부모 타입으로 선언된 변수에도 할당할 수 있다. 단, 부모 타입의 변수로 사용할 때는, 실제 객체를 만들 때 사용한 자식 타입에 있는 함수를 호출할 수 없다.

>참고, 상속을 받을 때 여러 클래스를 상속받을 수는 없다. 오직 하나의 클래스만을 상속받을 수 있다.

### super()

부모 클래스로부터 상속받은 필드나 메소드를 자식 클래스에서 참조하여 사용하고 싶을 때 사용하는 키워드

### 오버로딩(overloading) vs 오버라이딩(overriding)

- 오버로딩이란 한 클래스 내에 동일한 이름의 메소드를 여러개 정의하는 것
- 오버로딩의 조건
    - 메소드 이름이 동일해야 한다.
    - 매개변수의 개수 혹은 타입이 달라야 한다.


- 오버라이딩이란 부모 클래스로부터 상속받은 메소드의 내용을 변경하는 것
- 상속받은 메소드를 그대로 사용하기도 하지만, 필요에 의해 변경해야할 경우 오버라이딩 해야한다.
- 오버라이딩의 조건
    - 부모 클래스의 메소드와 이름이 같아야 한다.
    - 부모 클래스의 메소드와 매개변수가 같아야 한다.
    - 부모 클래스의 메소드와 반환타입이 같아야 한다.


### 오버로딩 vs 오버라이딩 (비교)

```plain/text
오버로딩 : 기존에 없는 새로운 메소드를 정의하는 것
오버라이딩 : 상속받은 메소드의 내용을 변경하는 것
```