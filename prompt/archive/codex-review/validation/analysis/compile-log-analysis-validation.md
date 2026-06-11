# compile-log-analysis.md 검토 결과

## 1. 총평

`compile-log-analysis.md`는 “컴파일 로그 기반 분석”이라는 기본 목적은 비교적 분명하고, `실제 소스 수정 금지`, `실제 pom.xml 수정 금지`, `compile 로그에 없는 오류를 생성하지 않는다` 같은 핵심 통제도 들어 있어 안전한 편입니다. 또한 Java 버전, dependency, import/package, Spring XML wiring, iBatis/MyBatis 영향으로 분석 축을 나눈 점도 실무적으로 유용합니다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:12)

다만 실제 전자정부프레임워크 3.x → 4.x 전환용 프롬프트로 보면 아직 보수성이 충분하지 않습니다. 가장 큰 문제는 `pom.xml`, `실제 Java/XML 소스`, `@Codebase`, `추론`이 우선순위에 남아 있어 “로그 분석 프롬프트”가 “원인 추정 프롬프트”로 확장될 여지가 있다는 점입니다. 또 eGovFrame 4.3/4.5, Java 8/17/21, WAS 차이, `javax/jakarta` 단정 금지, 반복 오류의 대표/파생 구분, 조치 방향과 수정 지시의 분리 같은 중요한 실무 기준이 부족합니다. 결론적으로 `일부 보완 후 사용 권장`보다는 `구조 재정비 필요`에 가깝습니다.

## 2. 잘 작성된 부분

- `분석만 수행`, `실제 소스 수정은 하지 않는다`가 분명하다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:26)
- `실제 오류 메시지 기준으로만 분석`, `없는 class/package 생성 금지`, `compile 로그에 없는 오류 생성 금지`는 유지해야 할 핵심 통제다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:93)
- Java 버전 오류, dependency 오류, import/package 오류, Spring/XML wiring 오류를 나눠 본 점은 컴파일 로그 분류 기준으로 적절하다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:106)
- `root cause는 최초 오류 우선`, `연쇄 오류 분리`, `여러 가능성이 있으면 추가 확인 필요`는 로그 분석 프롬프트에 잘 맞는 규칙이다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:270)
- `Spring Boot`, `Gradle`, `Java 17 업그레이드`를 기본 해법처럼 제안하지 못하게 막은 점은 과잉 처방 방지에 도움된다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:95)

## 3. 보완이 필요한 부분

| 위치/섹션 | 현재 문제점 | 개선 방향 | 중요도 |
|---|---|---|---|
| `## 분석 우선순위` | `pom.xml`, `실제 Java/XML 소스`, `@Codebase`, `추론`이 포함되어 있어 로그 바깥 내용을 근거로 원인을 확정할 여지가 있다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:77) | `로그 우선`, `stack trace`, `개발자가 함께 제공한 관련 설정/소스 조각` 정도로 좁히고, 명시 근거 없으면 `확인 필요`로 처리하도록 바꿔야 한다. | 높음 |
| `## 목표` / `## 분석 목적` | “원인/영향/조치 방향”과 “실제 수정 지시”의 경계가 명확히 적혀 있지 않다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:14) | `조치 방향은 검토 후보 수준으로만 작성하고, dependency 추가/버전 변경/소스 수정 지시는 하지 않는다`를 명시해야 한다. | 높음 |
| `## 분석 대상 오류 유형` | `method signature mismatch`, `constructor mismatch`, `annotation processor`, `module path/classpath`, `resource filtering`, `encoding`, `test-compile` 오류가 빠져 있다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:106) | 실제 javac/maven 컴파일 실패 유형을 더 세분화해야 한다. | 높음 |
| `## Import/Package 오류 분석 기준` | `javax`, `jakarta`, `egovframework`, `org.egovframe`을 보지만 “무조건 전환 대상 아님” 규칙이 약하다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:174) | `javax 오류는 pom/WAS/JDK/소스 중 어디서 기인했는지 로그로 확인되지 않으면 단정 금지` 같은 문구가 필요하다. | 높음 |
| `## Java 버전 분석 기준` | Java 버전 항목은 있으나 eGovFrame 4.3/4.5, Java 8/17/21, WAS 조합 차이를 반영하지 않는다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:127) | `환경 차이에 따라 동일 오류의 해석이 달라질 수 있음`을 명시하고, 절대 단정 대신 `호환성 확인 필요`를 기본 표현으로 써야 한다. | 높음 |
| `## Dependency 오류 분석 기준` | `Could not resolve artifact` 등을 보지만, repository 문제와 실제 라이브러리 누락, 폐쇄망, parent pom 누락, profile 비활성 문제를 구분하지 못한다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:152) | `동일 오류라도 원인 후보를 분리`하고, `pom-analysis`/`dependency-analysis`로 넘길 조건을 정의해야 한다. | 중간 |
| `## Spring/XML Wiring 오류 분석 기준` | compile-log 프롬프트인데 런타임 bean 오류까지 넓게 잡고 있다. `BeanCreationException`, `NoSuchBeanDefinitionException`은 빌드 로그가 아니라 실행 로그일 수도 있다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:192) | `compile 단계에서 실제로 등장한 경우만 분석`, `실행 로그인지 compile 로그인지 먼저 구분` 규칙이 필요하다. | 높음 |
| `## 출력 형식` | `오류 메시지`, `root cause 후보`, `영향도`, `수동검토`만 있고 `근거 로그`, `대표 오류 여부`, `파생 오류 여부`, `조치 방향`, `확정도`가 없다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:225) | 후속 전환 작업에 재사용하려면 컬럼을 더 구조화해야 한다. | 높음 |
| `## 마지막 요약` | `우선 수정 필요 항목` 표현은 수정 지시처럼 읽힐 수 있다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:304) | `우선 확인 필요 항목` 또는 `우선 검토 대상`으로 완화하는 편이 안전하다. | 중간 |
| `## 금지 사항` | 본문에 비해 하단 금지사항이 약하고, `dependency 추가`, `버전 변경`, `라이브러리 교체`, `javax→jakarta 직접 권고` 금지가 명시되지 않았다. | 금지사항을 더 직접적으로 보강해야 한다. | 높음 |

## 4. 누락된 검토 기준

전자정부프레임워크 전환과 컴파일 로그 분석 관점에서 아래 기준은 추가되는 편이 좋습니다.

- `compile 로그`와 `runtime/startup 로그`를 구분하는 규칙
- `test-compile`와 `main compile` 구분 규칙
- `대표 오류`와 `파생 오류` 구분 규칙
  - 같은 missing class로 수십 건 발생해도 대표 오류 1건과 연쇄 오류로 묶기
- `원인 후보`와 `조치 방향` 분리 규칙
- `확정`, `가능성`, `확인 필요` 같은 확정도 레벨
- `javax/jakarta` 해석 기준
  - import 문제인지
  - dependency 문제인지
  - container/WAS 제공 문제인지
  - JDK 문제인지
- `egovframework.rte` vs `org.egovframe.rte` 관련 오류 해석 기준
  - 이름만 다르다고 자동 rename 대상으로 단정 금지
- `iBatis/MyBatis` 관련 오류 세분화
  - `SqlMapClient`, `EgovAbstractDAO`, `EgovComAbstractDAO`, `SqlSessionTemplate`, `MapperScannerConfigurer`
- `JDK/WAS 환경 차이`
  - Java 8/17/21
  - eGovFrame 4.3/4.5
  - Tomcat/JEUS/WebLogic 차이
- `annotation processor` 관련 컴파일 오류
  - Lombok, MapStruct, Querydsl 등
- `method signature mismatch`, `constructor mismatch`, `generic type mismatch` 분류
- `resource/encoding/build plugin` 계열 컴파일 실패 분류
- `profile 미활성`, `parent pom 누락`, `dependencyManagement 미적용` 가능성 표시
- `후속 분석 연결 조건`
  - dependency 오류면 `pom-analysis`/`dependency-analysis`
  - import/package 구조면 `package-scan-analysis`
  - Spring bean이면 `spring-xml-analysis`
  - DAO/SqlMap이면 `dao-analysis`/`sqlmap-analysis`

## 5. 할루시네이션 또는 과잉 판단 위험

가장 큰 위험은 `## 분석 우선순위`입니다. 여기서 `pom.xml`, `실제 Java/XML 소스`, `@Codebase`, `추론`이 들어가 있기 때문에, Qwen이 로그에 명시되지 않은 원인을 바깥 자료를 보고 사실처럼 정리할 수 있습니다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:77)

또 다른 위험은 `javax/jakarta`, `egovframework/org.egovframe`, `SqlMap/MyBatis` 같은 전환 민감 키워드를 보면 Qwen이 너무 빨리 “전환 누락”으로 해석할 수 있다는 점입니다. 현재 문구만으로는 “그럴 가능성”을 충분히 낮추지 못합니다. 예를 들어 `package javax.servlet does not exist`가 떠도 실제 원인은 JDK, scope, container provided, pom profile, IDE classpath, build plugin 중 하나일 수 있습니다.

`Spring/XML Wiring 오류`도 위험합니다. `BeanCreationException`이나 `NoSuchBeanDefinitionException`은 보통 실행/테스트 단계에서 더 흔한데, compile 로그 분석 프롬프트가 이를 같은 무게로 다루면 로그 종류를 혼동할 수 있습니다. [compile-log-analysis.md](/Users/taeyong/project/cf-egovboard-war/prompt/qwen/analysis/compile-log-analysis.md:192)

마지막으로 `우선 수정 필요 항목` 같은 표현은 분석 결과를 수정 지시처럼 보이게 만들 수 있습니다. 이 프롬프트의 목적은 수정이 아니라 원인 분류와 검토 우선순위화여야 합니다.

## 6. 권장 보완 문구

`compile-log-analysis.md`에 직접 반영 가능한 문구 예시는 아래와 같습니다.

```md
## 분석 우선순위

다음 우선순위를 따른다.

1. 실제 compile 오류 로그
2. stack trace
3. 동일 로그 내 앞선 오류와 뒤따르는 연쇄 오류 관계
4. 개발자가 함께 제공한 pom.xml 또는 관련 소스 조각
5. 명시적 근거가 없는 경우 "확인 필요" 처리

주의:
- compile 로그에 직접 나타나지 않은 원인을 사실처럼 단정하지 않는다.
- pom.xml 또는 소스는 로그 해석의 보조 근거로만 사용한다.
- @Codebase 전체 탐색 결과만으로 root cause를 확정하지 않는다.
```

```md
## 원인/조치 방향 구분 규칙

- "원인 후보"와 "조치 방향"을 반드시 분리하여 작성한다.
- 조치 방향은 수정 지시가 아니라 검토 필요 항목 수준으로만 작성한다.
- dependency 추가, version 변경, library 교체, import 변경, package rename을 직접 실행 지시로 작성하지 않는다.
```

```md
## javax/jakarta 및 eGovFrame 전환 해석 규칙

- javax 관련 오류가 발생해도 즉시 jakarta 전환 대상으로 단정하지 않는다.
- org.egovframe 관련 오류가 발생해도 자동 rename 또는 전환 누락으로 단정하지 않는다.
- 동일 오류는 JDK, dependency scope, WAS/container 제공 범위, parent pom/profile, 실제 소스 import 중 어디에서 비롯됐는지 로그 근거가 있는 경우에만 좁혀서 작성한다.
- 로그만으로 특정 원인을 확정할 수 없으면 "호환성 확인 필요" 또는 "추가 확인 필요"로 표시한다.
```

```md
## 반복 오류 처리 규칙

- 동일한 root cause에서 파생된 반복 오류는 대표 오류와 파생 오류로 구분한다.
- 같은 missing class/package로 다수 파일이 실패한 경우 대표 오류 1건을 먼저 기록하고 나머지는 연쇄 오류로 요약한다.
- 오류 건수와 원인 건수를 구분해서 집계한다.
```

```md
## 출력 형식

| 오류 유형 | 대표 여부 | 파일 | 위치 | 오류 메시지 | 원인 후보 | 조치 방향 | 영향 범위 | 확정도 | 수동검토 |
|---|---|---|---|---|---|---|---|---|---|

확정도는 다음 중 하나로 작성한다.
- 로그로 확인
- 가능성 있음
- 확인 필요
```

```md
## 금지 사항

- dependency 추가 직접 권장 금지
- dependency version 변경 직접 권장 금지
- 라이브러리 교체 직접 권장 금지
- javax → jakarta 일괄 변경 권장 금지
- egovframework → org.egovframe 일괄 rename 권장 금지
- compile 로그에 없는 root cause 생성 금지
- 실제 소스 확인 없이 메서드/클래스/bean 존재를 단정하지 않는다
```

## 7. 최종 판단

- 구조 재정비 필요

## 주의사항

- 검토 대상 파일을 직접 수정하지 않았다.
- 실제 프로젝트 소스도 수정하지 않았다.
- 검토 결과만 Markdown으로 작성했다.
- 수정 위치는 가능한 한 `compile-log-analysis.md`의 실제 섹션명을 기준으로 제시했다.
- 문체보다 Qwen의 오분석, 과잉 추정, 과잉 수정 유도 위험을 중심으로 검토했다.