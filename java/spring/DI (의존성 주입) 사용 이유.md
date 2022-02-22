# 스프링에서 DI (의존성 주입) 를 사용하는 이유는?

> 강한 결합의 문제점을 해결하기 위함이다.

## 예시

- `Repository1` 객체 생성 시 DB 접속 id, pw를 받아서 DB 접속 시 사용

  - 생성자에 DB 접속 id, pw를 추가

    ```java
    public class Repository1 {

        public Repository1(String id, String pw) {
        // DB 연결
        Connection connection = DriverManager.getConnection("jdbc:h2:mem:springcoredb", id, pw);
        }
    }
    ```

- `Controller 5개`가 각각 `Service1` 을 생성하여 사용

- `Repository1` 생성자 변경에 의해 . . .

    => `모든 Controller` 와 `모든 Service`의 코드 변경이 필요해짐

<img src="https://teamsparta.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3cdcb5ab-5b23-473b-95f0-18baaa1679d0%2FUntitled.png?table=block&id=7481960e-a4f3-414e-a394-09fba1cf678f&spaceId=83c75a39-3aba-4ba4-a792-7aefe4b07895&width=1820&userId=&cache=v2">


