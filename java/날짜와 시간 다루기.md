# 날짜와 시간 다루기

## Java에서의 날짜와 시간

>java.time 패키지

```
패키지(package)란?
간단하게는 클래스의 묶음이라고 할 수 있다. 패키지에는 클래스 혹은 인터페이스를 포함시킬 수 있으며 관련된 클래스끼리 묶어 놓음으로써 클래스를 효율적으로 관리할 수 있다.
```

### 종류

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("now()를 활용하여 생성");
        LocalDate date = LocalDate.now();  // 현재날짜
        LocalTime time = LocalTime.now();  // 현재 시간
        LocalDateTime dateTime = LocalDateTime.now();  // 현재 날짜와 시간

        System.out.println(date);
        System.out.println(time);
        System.out.println(dateTime);

        System.out.println("of()를 활용하여 생성");
        LocalDate newDate = LocalDate.of(2021, 03, 29);
        LocalTime newTime = LocalTime.of(22, 50, 55);

        System.out.println(newDate);
        System.out.println(newTime);
    }
}
```

```
now() vs of()
위 예제에서 사용한 now() 와 of()는 객체를 생성할 때 사용된다.
now()는 현재의 날짜 시간을, of()는 지정하는 값이 필드에 담겨진다.
```

## 날짜와 시간의 형식 수정

```java
DateTimeFormatter formatter = DateTimeFormatter.ofLocalizedTime(FormatStyle.SHORT);
String shortFormat = formatter.format(LocalTime.now());
System.out.println(shortFormat);  // 오후 11:02
```
- `LocalDate.now()`를 했을 때와는 다르게 오전/오후가 추가되었으며 보다 직관적인 형태가 되었다.
- 형식을 변환하는데 사용한 `DateTimeFormatter`클래스는 SHORT이외에도 다양한 FormatStyle 종류가 있다.

- 사용하고자 하는 형식이 없거나 생각하는 형식이 있을 경우 직접 지정도 가능하다.
 
```java
DateTimeFormatter newFormatter = DateTimeFormatter.ofPattern("yyyy/MM/dd");
String myDate = newFormatter.format(LocalDate.now());
System.out.println(myDate);  // 2022/02/16
```

## 날짜와 시간의 차이 계산

```java
LocalDate today = LocalDate.now();  // 2022 02 16
LocalDate birthday = LocalDate.of(2022, 3, 16);
Period period = Period.between(today, birthday);
System.out.println(period.getMonths()); // 1
System.out.println(period.getDays());  // 0
```
- 오늘 일자와 생일 일자간의 날짜 차이를 계산하기 위해서는 between()을 사용하면 구할 수 있다. (between 이외에도 until()로 구할 수도 있다.)
