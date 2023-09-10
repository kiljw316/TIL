# 자료조사

## **컨테이너란**

- 컨테이너는 **소프트웨어를 실행**하는 데 필요한 특정 버전의 프로그래밍 언어 런타임 및 라이브러리와 같은 **종속 항목**과 애플리케이션 코드를 함께 포함하는 **경량** **패키지**임
- 또한 운영체제 수준에서 CPU, 메모리, 스토리지, 네트워크 **리소스를 쉽게 공유**할 수 있게 해주며 컨테이너가 실제로 실행되는 환경에서 **애플리케이션을 추상화할 수 있는 논리 패키징** 메커니즘을 제공함

## 컨테이너의 주요 특징과 개념

1. 환경 격리
    - 호스트 시스템과의 완전한 격리
    - 다른 컨테이너나 호스트 시스템에 영향을 주지 않음
    - 이를 통해 의존성 충돌로부터 애플리케이션을 보호
2. 이식성
    - 동일한 이미지를 다양한 환경에서 실행할 수 있음
    - 개발 환경에서 테스트한 컨테이너를 운영 환경에서도 동일하게 실행할 수 있음
    - 클라우드, 로컬 머신, 개발자의 노트북 등 어디에서든 배포할 있음
3. 가벼움
    - 자체 운영 체제 OS는 포함하지 않기 때문에 가상 머신(VM)보다 가벼움
    - 호스트 시스템의 커널을 공유하며 자체 운영 체제 이미지를 가지지 않기 때문에 더 효율적으로 자원을 활용할 수 있음
4. 빠른 시작과 중지
    - 실행 된 OS에서 응용 프로그램 본체와 미들웨어를 실행하기만 하면되기 때문에 응용 프로그램의 시작 시간은 VM보다 크게 단축됨
    - 컨테이너를 실행하는 것은 OS 입장에서 보면 단순하게 프로세스를 시작하는 것이기 때문임

## 컨테이너의 이점

1. 책임 분리
    - 개발자: 애플리케이션의 로직과 종속 항목에 집중
    - IT 운영팀: SW 버전 및 구성과 같은 애플리케이션의 세부 요소 대신 배포 및 관리에 집중
2. 워크로드 이동성
    - 컨테이너는 OS를 가리지 않고 어느 환경에서나 구동하여 개발 및 배포가 크게 쉬워짐
3. 애플리케이션 격리
    - 컨테이너는 OS 수준에서 서버 리소스를 가상화함
    - 개발자에게 다른 애플리케이션으로부터 논리적으로 격리된 OS 환경을 제공

## 도커란

- **컨테이너 기반의 오픈소스 가상화 플랫폼**
- Docker는 소프트웨어를 **컨테이너**라는 표준화된 유닛으로 패키징하며, 이 컨테이너에는 라이브러리, 시스템도구, 코드, 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함되어 있음
- 따라서 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼임
- Docker를 사용하면 환경에 구애받지 않고 애플리케이션을 신속하게 배포 및 확장할 수 있으며 코드가 문제없이 실행될 것임을 확신할 수 있음

### 도커 이미지

- 컨테이너 실행에 필요한 파일과 설정값등을 포함하고 있는 것
- 컨테이너는 이미지를 실행한 상태라고 볼 수 있음
- 추가되거나 변하는 값은 컨테이너에 저장됨
- 컨테이너의 상태가 바뀌거나 삭제되더라도 이미지는 변하지 않고 그대로 남아있음

### Dockerfile

- 도커 이미지를 만들기 위한 파일
- 컨테이너 실행에 필요한 의존성과 설정값 등을 Dockerfile로 관리

## 도커 컴포즈란

- 여러 개의 **도커 컨테이너**를 정의하고 실행하기 위한 도구
- YAML 파일을 사용하여 애플리케이션 서비스를 구성
- 단일 명령을 사용하여 구성한 파일을 통해 모든 서비스를 생성하고 시작
- 주로 다수의 도커 컨테이너로 이루어진 복잡한 애플리케이션 스택을 간단하게 관리할 때 사용
- 어플리케이션의 전체 라이프사이클 관리를 위한 커맨드도 있음
    - 서비스 시작, 중지 및 재구축
    - 실행 중인 서비스 상태 보기
    - 실행 중인 서비스의 로그 출력 스트리밍
    - 서비스에서 일회성 명령 실행

### Docker Compose의 주요 특징과 개념

1. YAML 파일
    - Docker Compose 설정은 YAML(YAML Ain't Markup Language) 포맷으로 정의됨
    - 이 파일에는 컨테이너의 이미지, 환경 변수, 포트 포워딩 및 볼륨 마운트 등과 같은 컨테이너 관련 정보가 포함됨
2. 서비스
    - Docker Compose에서 각 컨테이너는 서비스로 정의됨.
    - 서비스는 하나 이상의 컨테이너로 구성될 수 있으며, 동일한 서비스에 속하는 컨테이너는 함께 실행 및 관리됨
3. **복제**
    - Docker Compose를 사용하여 동일한 서비스를 여러 번 실행할 수 있음.
    - 이를 통해 여러 개의 인스턴스를 병렬로 실행하고 로드 밸런싱 등을 수행할 수 있음
4. **네트워크**
    - Docker Compose는 컨테이너 간 통신을 위한 가상 네트워크를 자동으로 생성함
    - 서비스 간에 쉽게 통신할 수 있음
5. **볼륨**
    - 컨테이너와 호스트 시스템 간 데이터 공유를 위해 볼륨을 사용할 수 있음
    - Docker Compose는 볼륨을 정의하고 관리하는 기능을 제공함

### phase 별 컴포즈 설정 방법

1. 환경별로 독립적인 컴포즈 파일 생성
    1. **`docker-compose.dev.yml`**, **`docker-compose.stage.yml`**, **`docker-compose.prod.yml`**
    2. 각각의 컴포즈 파일은 각 환경에 필요한 이미지 및 환경 변수와 같은 설정을 다르게 정의
    3. 환경에 따라 다른 컴포즈 파일을 실행
2. 공통파일 및 환경별 오버라이드 파일 생성
    1. **`docker-compose.yml`**, **`docker-compose.override.dev.yml`**, **`docker-compose.override.prod.yml`**
    2. 공통파일: 모든 환경에 공통적으로 적용될 내용
    3. 오버라이드 파일: 특정 환경에만 적용하고 싶은 변경 내용

## **GitHub Actions**

- 빌드, 테스트 및 배포 파이프라인을 자동화활 수 있는 CI/CD 플랫폼임
- 개발 프로세스를 자동화하고 개발자들이 코드 변경 사항을 안전하게 통합하고 배포할 수 있음
- 팀 협업을 개선하고 소프트웨어의 품질을 유지하며 배포 주기를 빠르게 만드는 데 도움이 됨
- GitHub의 일부로 제공되므로 GitHub 저장소에서 쉽게 설정하고 사용할 수 있음
- 저장소에서 이벤트가 발생할 때 워크플로를 실행함
- GitHub은 워크플로를 실행하기 위한 여러 OS 가상 머신을 제공

### **GitHub Actions의 구성 요소**

1. **워크플로(Workflows)**
    - GitHub Actions는 워크플로라고 하는 자동화 작업 단위를 정의
    - 워크플로는 GitHub 리포지토리에 저장되며, 이벤트(예: 코드 푸시, 이슈 생성)에 응답하여 실행
2. **이벤트 트리거(Event Triggers)**
    - GitHub Actions 워크플로는 특정 이벤트에 응답하여 실행됨
    - 예를 들어, 코드 푸시, 이슈 생성, 레이블 변경 등의 이벤트가 트리거로 사용될 수 있음
3. **작업(Jobs)**
    - 워크플로는 하나 이상의 작업으로 구성됨
    - 각 작업은 독립적으로 실행될 수 있으며, 작업 간에 종속성을 정의할 수 있음
4. **액션(Actions)**
    - 액션은 작업의 구성 요소로, 특정 작업을 수행하는 데 사용됨
    - GitHub Actions 커뮤니티에서 제공하는 많은 사전 정의된 액션을 사용하거나, 자체 액션을 작성하여 워크플로를 사용자 지정할 수 있음
5. **환경(Environment)**
    - 각 작업은 환경 변수를 사용하여 설정을 구성할 수 있음
    - 이를 통해 비밀 정보(예: API 키, 비밀 번호)를 안전하게 관리하고 사용할 수 있음
6. **캐시(Cache)**
    - 워크플로는 종속성을 빌드하고 테스트하는 데 많은 시간이 걸릴 수 있음
    - 캐시를 사용하여 중복 작업을 피하고 빌드 시간을 단축할 수 있음
7. **시크릿(Secrets)**
    - GitHub Actions은 보안을 위해 시크릿을 지원함
    - 시크릿을 사용하면 중요한 정보를 환경 변수로 안전하게 전달할 수 있음
8. **프로비저닝(Provisioning)**
    - 워크플로를 사용하여 서버, 컨테이너, 애플리케이션 등을 자동으로 프로비저닝하고 배포할 수 있음

## 정리

- 컨테이너는 종속 항목은 모두 포함하면서 외부 시스템과 완전히 격리된 환경으로 패키징함
    - 격리된 환경으로 인해 개발자는 어플리케이션 개발에 집중할 수 있음
- 컨테이너 플랫폼(docker)을 통해 컨테이너를 쉽게 구축, 테스트 및 배포할 수 있음
- 여러 컨테이너는 컴포즈 등의 멀티 컨테이너 도구나 k8s 등의 컨테이너 자동화 시스템을 활용할 수 있음
- Github Actions 등의 CI/CD 플랫폼을 통해 위의 모든 작업들을 중앙 집중화하여 자동화할 수 있음

## 참고 자료

- 컨테이너
    - [https://cloud.google.com/learn/what-are-containers?hl=ko](https://cloud.google.com/learn/what-are-containers?hl=ko)
    - [http://www.opennaru.com/openshift/container/benefits-of-container/](http://www.opennaru.com/openshift/container/benefits-of-container/)
    - [https://www.docker.com/resources/what-container/](https://www.docker.com/resources/what-container/)
- 도커
    - [https://www.redhat.com/ko/topics/containers/what-is-docker](https://www.redhat.com/ko/topics/containers/what-is-docker)
    - [https://aws.amazon.com/ko/docker/](https://aws.amazon.com/ko/docker/)
    - [https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html](https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)
- 도커 컴포즈
    - [https://docs.docker.com/compose/](https://docs.docker.com/compose/)
    - [https://www.yes24.com/Product/Goods/111408749](https://www.yes24.com/Product/Goods/111408749)
- Github Actions
    - [https://docs.github.com/ko/actions](https://docs.github.com/ko/actions)