# Java Collection

## 컬렉션 프레임워크란?

- <U>다수의 데이터를 다루기 위한 자료구조를 표현하고 사용하는 클래스의 집합을 의미한다.</U>
- 컬렉션 프레임워크의 모든 클래스는 `Collection` interface를 구현(implement)하는 클래스 또는 인터페이스이다.

## 컬렉션 인터페이스와 자료구조

`Collection`은 모든 자료구조가 구현하는 인터페이스이다.

1. List: 순서가 있는 데이터의 집합이며 데이터의 중복을 허용한다.

   - ArrayList, LinkedList, Stack 등

2. Set: 순서를 유지하지 않는 데이터의 집합이며 데이터의 중복을 허용하지 않는다.

   - HashSeet, TreeSet 등

3. Map: 키(key)와 값(value)의 쌍으로 이루어진 데이터의 집합이다. 순서는 유지되지 않으며 키는 중복이 허용되지 않고 값은 중복을 허용한다.

   - HashMap, TreeMap 등

4. Stack: 마지막에 넣은 데이터를 먼저 꺼내는 자료구조이다. LIFO(Last In First Out)

   - Stack, ArrayDeque 등

5. Queue: 먼저 넣은 데이터를 먼저 꺼내는 자료구조이다. FIFO(First In First Out)
   - Queue, ArrayDeque 등

컬렉션 인터페이스에는 컬렉션 클래스에 저장된 데이터를 읽고, 추가하고 삭제하는 등 데이터를 다루는데 기본적인 메서드들을 정의하고 있다.

## 리스트

- 순서가 있는 나열된 데이터를 표현한다.
- ArrayList는 배열을 이용하여 데이터를 저장하는 List 인터페이스이다.

```java
public class Main {
    public static void main(String[] args) {
        List list = new ArrayList(10);
        list.add(1);
        list.add(5);
        list.add(4);
        list.add(11);
        list.add(10); // ArrayList에 값 한개씩 입력
        System.out.println(list); // [1,5,4,11,10]

        Collections.sort(list); // list 정렬
        System.out.println(list); // [1,4,5,10,11]

        System.out.println(list.size()); // arrayList의 크기 출력

        arrayList.remove(4); // 인덱스를 활용하여 해당하는 값 제거
        System.out.println(list);

        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i)); // get을 이용하여 값 1개씩 출력
        }
				for (int current : list) {
						System.out.println(current);
        }

    }
}
```

## 셋

- 순서를 유지하지 않는 데이터의 집합이며 데이터의 중복을 허용하지 않는다.
- HashSet은 Set 인터페이스를 구현한 대표적인 컬렉션이다.

```java
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Set;

public class Main {
    public static void main(String[] args) {
        Set<Integer> integerSet = new HashSet<>(); // Collection의 자료형에는 primitive 타입은 올 수 없습니다. primitive 타입에 해당하는 class 가 존재하니 그것을 사용하세요.
        integerSet.add(1);
        integerSet.add(3);
        integerSet.add(2);
        integerSet.add(9);// 하나씩 값을 삽입합니다.
        System.out.println(integerSet); // 출력을 해보면 순서가 지켜지지 않는 것을 알 수 있습니다.

        Set<String> stringSet = new HashSet<>();
        stringSet.add("LA");
        stringSet.add("New York");
        stringSet.add("LasVegas");
        stringSet.add("San Francisco");
        stringSet.add("Seoul");
        System.out.println(stringSet);

        stringSet.remove("Seoul"); //Seoul을 HashSet에서 제거해보겠습니다.
        System.out.println(stringSet);

        ArrayList<String> target = new ArrayList<String>();
        target.add("New York");
        target.add("LasVegas");//제거할 항목을 ArrayList에 삽입하겠습니다.
        stringSet.removeAll(target);//제거항목에 삽입된 도시들을 삭제하겠습니다.
        System.out.println(stringSet);

        System.out.println("LA가 포함되어있나요? " + stringSet.contains("LA"));
        System.out.println("LA가 포함되어있나요? " + stringSet.contains("LasVegas"));
        //LA가 HashSet에 포함되어있으면 true를, 그렇지 않으면 false를 반환합니다.

        System.out.println("현재 HashSet의 크기는 : " + stringSet.size() + "입니다.");
        //HashSet의 크기를 반환합니다.

        stringSet.clear();//HashSet의 모든 아이템들을 삭제합니다.
        System.out.println(stringSet);
    }
}
```

## 맵

- HashMap은 키(key)와 값(value)을 하나의 데이터로 저장하는 특징을 가진다.
- 이를 통하여 해싱(hashing)을 가능하게 하여 데이터를 검색하는데 뛰어난 성능을 보인다.

```java
public class Main {
    public static void main(String[] args) {
        Map<Integer, String> map = new HashMap<>();
        map.put(1, "apple");
        map.put(2, "berry");
        map.put(3, "cherry");

        System.out.println(map);

        System.out.println("1st in map: " + map.get(1));

        map.remove(2);
        System.out.println(map);
        System.out.println(map.containsKey(2));
        System.out.println(map.containsValue("cherry"));

        map.clear();
        System.out.println(map);
    }
}
```

## 스택

- 스택이란 마지막에 저장한 데이터를 가장 먼저 꺼내는 자료구조이다. 이것을 <U>LIFO(Last In First Out)</U> 라고 한다.
- 스택의 예
  - 웹브라우저의 앞 뒤 페이지 이동 / 그릇 쌓기

```java
public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(3);
        stack.push(5);
        stack.push(7);
        System.out.println(stack); // Stack을 출력합니다

        System.out.println(stack.peek()); // Stack의 가장 상단 값을 출력합니다.(삭제는 하지 않습니다.)
        stack.pop(); // Stack의 가장 상단 값을 제거합니다.
        System.out.println(stack);
        System.out.println(stack.size()); // Stack의 크기를 반환합니다.
        System.out.println(stack.contains(1)); // Stack에 1이라는 값이 있으면 true를, 그렇지 않으면 false를 반환합니다.
        System.out.println(stack.empty()); // STack이 비어있으면 true를, 그렇지 않으면 false를 반환합니다.
        System.out.println(stack);
    }
}
```

## 큐

- 큐는 처음에 저장한 데이터를 가장 먼저 꺼내게 되는 <U>FIFO(First In First Out)</U> 구조로 되어있다.
- 큐의 예
    - 은행 창구 줄서기 / 인쇄작업 대기목록

```java
public class Main {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(1);
        queue.add(3);
        queue.add(5);//Queue에 값 삽입합니다.
        System.out.println(queue);//Queue 출력합니다.
        System.out.println(queue.poll()); // Queue에서 객체를 꺼내서 반환합니다.
        queue.add(7);
        queue.add(11);
        queue.add(9);
        System.out.println(queue);
        System.out.println(queue.peek()); //Queue에서 삭제 없이 요소를 반환합니다.
        System.out.println(queue);
    }
}
```
## ArrayDeque

- deque는 양 끝에서 삽입과 삭제가 가능하다.

```java
public class Main {
    public static void main(String[] args) {
        ArrayDeque<Integer> arrayDeque = new ArrayDeque<>(); // ArrayDeque를 이용한 선언(제네릭스 이용)
        arrayDeque.addFirst(1);
        arrayDeque.addFirst(2);
        arrayDeque.addFirst(3);
        arrayDeque.addFirst(4); // arrayDeque의 앞에 값을 삽입
        System.out.println(arrayDeque);

        arrayDeque.addLast(0); // arrayDeque의 끝에 값을 삽입
        System.out.println(arrayDeque);

        arrayDeque.offerFirst(10); // addFirst와 비슷하지만 큐의 크기 문제가 생길 때, offerFirst는 false를,
        // addFrist는 exception을 반환합니다.
        System.out.println(arrayDeque);

        arrayDeque.offerLast(-1); // arrayDeque의 끝에 값을 삽입
        System.out.println(arrayDeque);
        System.out.println(arrayDeque.size()); // 7


        System.out.println(arrayDeque.removeFirst()); // 첫번째 값을 제거하면서 그 값을 리턴
        System.out.println(arrayDeque.removeLast()); // 마지막 값을 제거하면서 그 값을 리턴
		    System.out.println(arrayDeque);
				System.out.println(arrayDeque.size()); // 5

        System.out.println(arrayDeque.pollFirst()); // 첫번째 값을 반환 및 제거하면서 그 값을 리턴
        System.out.println(arrayDeque);
				System.out.println(arrayDeque.size()); // 4

        System.out.println(arrayDeque.pollLast()); // 마지막 값을 반환 및 제거하면서 그 값을 리턴
        System.out.println(arrayDeque);
				System.out.println(arrayDeque.size()); // 3

        System.out.println(arrayDeque.peekFirst()); // 첫번째 값을 반환, 제거하지 않음
        System.out.println(arrayDeque.peekLast()); // 마지막 값을 반환, 제거하지 않음
				System.out.println(arrayDeque.size()); // 3
    }
}
```
