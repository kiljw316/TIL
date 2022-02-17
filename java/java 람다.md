# 람다

## 람다식(Lambda expression)이란

- "식별자 없이 실행 가능한 함수"라고 말할 수 있다. 즉, 함수의 이름을 따로 정의하지 않아도 곧바로 함수처럼 사용할 수 있고 문법이 간결하여 보다 편리할 방식이다. (익명 함수라고도 부른다.)

- 람다식이 코드를 보다 간결하게 만들어주는 역할을 하지만 그렇다고 무조건 좋다고만 이야기 할 수 는 없다.
- 이유는 ?

  - 람다를 사용하여서 만든 익명 함수는 재사용이 불가능하다.

  - 람다만을 사용할 경우 비슷한 메소드를 중복되게 생성할 가능성이 있으므로 지저분해질 수 있다.

## 람다식의 형식

- '->'의 의미는 매개변수를 활용하여 { } 안에 있는 코드를 실행한다는 것이다.

```markdown
[기존의 메소드 형식]
반환타입 메소드이름(매개변수 선언) {
수행 코드 블록
}

[람다식의 형식]
(매개변수 선언) -> {
수행 코드 블록
}
```

```java
public class Main {
    public static void main(String[] args) {
        ArrayList<String> strList = new ArrayList<>(Arrays.asList("korea", "japan", "china", "france", "england"));
        Stream<String> stream = strList.stream();
        stream.map(str -> str.toUpperCase()).forEach(System.out::println);
    }
}
```

## **이중 콜론 연산자** 또는 **메소드 참조 표현식**(method reference expression)

```java
public class Main {
    public static void main(String[] args) {
        List<String> cities = Arrays.asList("서울", "부산", "속초", "수원", "대구");
        cities.forEach(System.out::println);
    }
}
```

- 이중 콜론 연산자는 매개변수를 중복해서 사용하고 싶지 않을 때 사용하곤 한다.
- 사용 방법은 `[인스턴스]::[메소드명(또는 new)]`으로 사용한다.
- 스태틱 메소드인 경우 인스턴스 대신 클래스 이름으로 사용할 수 있다.
