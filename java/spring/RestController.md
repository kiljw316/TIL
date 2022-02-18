# RestController

>JSON 형식의 데이터를 응답할 떄 사용

## Rest

- 서버의 응답이 JSON 형식임을 나타낸다.
- HTML, CSS 등을 주고받을 때는 Rest를 붙이지 않는다.

## Controller

- 클라이언트의 요청을 전달받는 코드를 Controller 라고 부른다.
- JSON 만을 돌려주는 것은 RestController 라고 부른다.

## 예시

```java
@RestController
public class PracticeController {

    @GetMapping("/practice")  // Get 방식으로 정보를 요청할 때 사용한다.
    public Course getPractice() {
        Practice pratice = new practice("연습용 클래스");
        return practice;
    }
}
```

