## 접근제어자 (access modifier)

- 접근 제어자는 멤버 변수/함수 혹은 클래스에 사용되며 외부에서의 접근을 제한하는 역할을 한다.
- 종류
    - private : 같은 클래스 내에서만 접근이 가능하다.
    - default(nothing) : 같은 패키지 내에서만 접근이 가능하다.
    - protected : 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근이 가능하다.
    - public : 접근 제한이 전혀 없다.

- 접근 범위 정리

```
(좁음)                                                  (넓음)
private     →     default     →     protected     →     public
```

### 접근 제어자 사용 이유

- 객체지향 프로그래밍이란 객체들 간의 상호작용을 코드로 표현하는 것이다.
- 이때 객체들간의 관계에 따라서 접근 할 수 있는 것과 아닌 것, 권한을 구분할 필요가 생긴다.
- 클래스 내부에 선언된 데이터의 부적절한 사용으로부터 보호하기 위해서이다.
- 이런 것을 캡슐화(encapsulation)라고 한다.
- 접근 제어자는 캡슐화가 가능할 수 있도록 돕는 도구다.


## 추상 클래스

- 추상 클래스는 추상 메소드를 선언할 수 있는 클래스를 의미한다.
- 추상 클래스는 클래스와는 다르게 상속받는 클래스 없이 그 자체로 인스턴스를 생성할 수는 없다.

### 추상 메소드

- 추상 메소드는 설계만 되어있으며 수행되는 코드에 대해서는 작성이 안된 메소드이다.
- 미완성으로 남겨두는 이유는 상속받는 클래스 마다 반드시 동작이 달라지는 경우에 상속받는 클래스 작성자가 반드시 작성하도록 하기 위함이다.

### 추상 메소드 형식
```java
abstract 리턴타입 메소드 이름();
```

## 인터페이스

- 인터페이스는 객체의 특정 행동의 특징을 정의하는 간단한 문법이다.
- 인터페이스는 함수의 특징(method signature)인 접근제어자, 리턴타입, 메소드 이름만을 정의하고 함수의 내용은 없다.
- 인터페이스를 구현하는 클래스는 인터페이스에 존재하는 함수의 내용을 반드시 구현해야 한다.
- 쉽게말해 클래스에서 멤버가 빠진, 메소드 모음집이다.

### 인터페이스 형식

```java
interface 인터페이스명 {
    public abstract void 추상 메소드명();
}

인터페이스의 메소드는 추상 메소드, static 메소드, default 메소드 모두 허용된다.
(JDK 1.8 부터)
```

- interface type 으로 선언되어있는 부분에서는 실제 객체가 무엇이든지, interface에 정의된 행동만 할 수 있다.



## 인터페이스 vs 추상 클래스

### 인터페이스

- 구현하려는 객체의 동작의 명세
- 다중 상속 가능
- implements를 이용하여 구현
- 메소드 시그니처(이름, 파라미터, 리턴 타입)에 대한 선언만 가능

### 추상 클래스

- 클래스를 상속받아 이용 및 확장을 위함
- 다중 상속 불가능, 단일 상속
- extends를 이용하여 구현
- 추상 메서드에 대한 구현 가능

## 예외, 에러 처리

### 예외 처리란(Exception, Error Handling)

- 코드를 완벽하게 짰다고 해서 항상 프로그램이 성공적으로 도는 것은 아니다.
- 다양한 예외 상황이 발생했을 때, 이것에 대응하기 위해서 예외 처리 코드가 필요하다.

- 예외처리의 목적
    - 예외의 발생으로 인한 실행 중인 프로그램의 비정상 종료를 막기 위해서이다.
    - 개발자에게 알려서 코드를 보완할 수 있도록 하기 위해서 이다.

- 자바에서는 상속을 이용해서 모든 예외를 표현한다. 모든 예외 클래스는 `Throwable`의 자손 클래스 이다.

- `Throwable`에는 크게 두 종류의 자식 클래스가 있다.
    - `Error` 는 프로그램이 종료되어야 하는 심각한 문제를 표현한다.
    - 대부분 컴퓨터나 JVM이 시스템적으로 동작할 수 없는 상황을 표현한다.
    
    <br>

    >Java는 JVM내의 Heap이라는 메모리 공간을 운영체제로부터 할당 받아 사용합니다. 할당 받을 수 있는 최대 메모리 이상을 사용하면, JVM이 다운될 수 밖에 없습니다. 이 경우 OutOfMemoryError가 나면서 프로그램이 종료됩니다. 자바의 대표적인 에러 상황으로 줄여서 OOM이라고도 합니다.

    - `Exception`은 프로그램이 종료되지는 않지만 예외나 문제상황을 표현하기 위해 사용한다.

자바에 미리 정의 되어 있는 예외 클래스를 사용하거나, 필요한 것으로 표현할 수 없거나 구체적인 목적을 가진 예외를 정의하고 싶다면, `Throwable`또는 그 하위에 있는 예외 클래스를 상속받아서 자신만의 예외 클래스를 정의할 수 있다.


<img src="https://media.vlpt.us/images/codepark_kr/post/a70025be-d97d-4ba4-81de-bf9b8fe48d2b/ExceptionClassHierarchy.png">

예외 클래스 상속 관계 출처 [https://media.vlpt.us/images/codepark_kr/post/a70025be-d97d-4ba4-81de-bf9b8fe48d2b/ExceptionClassHierarchy.png](https://media.vlpt.us/images/codepark_kr/post/a70025be-d97d-4ba4-81de-bf9b8fe48d2b/ExceptionClassHierarchy.png)
    



### try-catch(-finally) 형식

```java
try {
    // 예외가 발생할 가능성이 있는 코드를 구현합니다.
} catch (FileNotFoundException e) {
    // FileNotFoundException이 발생했을 경우,이를 처리하기 위한 코드를 구현합니다.
} catch (IOException e) {
    // FileNotFoundException이 아닌 IOException이 발생했을 경우,이를 처리하기 위한 코드를 구현합니다.
} finally {
    // 예외의 발생여부에 관계없이 항상 수행되어야하는 코드를 구현합니다. finally 구문은 필수는 아닙니다.
    
}

만약, 예외가 발생하지 않는다면 try -> finally 순으로 실행된다.

```

예외는 중복 catch 블럭을 사용하여 다양한 예외처리를 수향할 수 있다. 중복 catch 블럭을 사용할 때는 먼저 선언된 catch 블럭부터 확인한다. 앞의 catch 블럭에서 잡혔다면, 뒤의 catch 블럭으로는 전파되지 않는다. 좁은 범위의 예외부터 앞에 선언하는 것이 좋다. 여기서 좁은 범위란 상속관계에서 자식 클래스에 위치할수록 좁은 범위이다. 예를 들어서 `IoException`이 발생할 것 같아 예외처리를 하고, 그 외의 예외도 예외처리를 하고 싶다면 `IoException`을 catch 하는 구문을 먼저, `Exception`을 catch 하는 구문을 그 뒤에 작성한다.


### try-with-resource 형식

- 입출력과 함께 자주 쓰이는 구문이다. 일반적으로 사용되었던 자원을 끝난 후에 닫아줘야 하는 것들이 존재하는데 여기서 try-catch 구문보다 편리한 것이 try-with-resource 문이다. 
- 기존의 try-catch 문은 자원을 닫을 때 close()를 사용해야 한다.
- try-with-resource 문은 try문을 벗어나는 순간 자동적으로 close()가 호출된다.

- 사용하는 방법은 try() 안의 입출력 스트림을 생성하는 로직을 작성할 때 해당 객체가 AutoClosable 인터페이스를 구현한 객체여야 한다.

<br>

```java
import java.io.FileOutputStream;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        try (FileOutputStream out = new FileOutputStream("test.txt")) {
            // test.txt file 에 Hello 를 출력
            out.write("Hello".getBytes());
            out.flush();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

<br>

```
AutoClosable 인터페이스
그럼 왜 AutoClosable 인터페이스를 사용해야할까요??바로 AutoClosable 인터페이스에는 예외가 발생할 경우 close()메소드를 호출하기로 정의되어있기 때문입니다.
```

### 메소드에서의 예외 선언

catch문을 이용해서 예외처리를 하지 않은 경우, 메소드에 throws로 예외가 발생할 수 있다는 것을 알려주어야 한다. throws 키워드가 있는 함수를 호출한다면, caller 쪽에서 catch와 관련된 코드를 작성해 주어야 한다.

```java
void method() throws IndexOutOfBoundsException, IllegalArgumentException {
    //메소드의 내용
}
```