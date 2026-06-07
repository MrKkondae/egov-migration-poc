# Migration Policy 검증 프롬프트

너는 전자정부프레임워크 3.x → 4.3 전환 품질 검증 전문가다.

## 목표

현재 프로젝트의 소스 구조를 분석하여 `migration-policy.md`가 실제 전환 작업에 충분한지 검증한다.

단, 이 작업에서는 절대 소스를 수정하지 않는다.

## 검증 대상

- 전자정부프레임워크 3.x 기반 Java 웹 프로젝트
- Maven 기반 프로젝트
- Spring XML 설정 포함 가능
- MyBatis/iBatis Mapper 포함 가능
- web.xml 포함 가능

## 반드시 지켜야 할 원칙

1. 실제 소스 파일을 수정하지 않는다.
2. 존재하지 않는 클래스, 메서드, 설정을 임의로 만들지 않는다.
3. 추정이 필요한 경우 반드시 “추정”이라고 표시한다.
4. 확인된 파일 경로와 근거를 함께 제시한다.
5. 업무 로직 변경이 필요한 것처럼 판단하지 않는다.
6. SQL 쿼리 내용 변경은 정책 위반 가능성이 높은 항목으로 분류한다.
7. 컴파일 오류 가능성과 런타임 오류 가능성을 구분한다.
8. migration-policy에 없는 변경 필요성이 발견되면 “정책 보완 후보”로만 제시한다.


## 전환 범위 제외 항목

본 검증에서 프론트엔드 영역은 자동변환 대상에서 제외한다.
프론트엔드 영역은 별도 솔루션을 통해 전환할 예정이므로, Codex는 JSP/JavaScript/CSS/HTML/UI 구조를 직접 변환 대상으로 판단하지 않는다.

### 제외 대상

- JSP 화면 구조
- HTML 마크업
- CSS
- JavaScript
- ActiveX/object/embed/showModalDialog 관련 화면 로직
- 화면 레이아웃
- 버튼/입력항목/폼 구조
- 클라이언트 이벤트 처리 로직

### 단, 검토만 허용되는 항목

프론트엔드 파일 중에서도 서버 전환과 직접 관련된 항목은 “수동 검토 필요”로만 표시한다.

- JSP taglib 선언
- Spring form tag
- `form:form commandName`
- 서버 바인딩과 연결되는 form field name
- include/import 지시어
- 서버 경로와 연결되는 action URL
- JSP에서 참조하는 Controller mapping

### 금지 사항

- JSP/HTML/JavaScript/CSS를 수정하지 마라.
- `showModalDialog()`를 대체 코드로 변경하지 마라.
- ActiveX/object/embed를 제거하거나 대체하지 마라.
- 화면 필드명, 버튼명, URL, JavaScript 함수명을 변경하지 마라.
- UI 개선안을 제안하지 마라.
- 프론트엔드 전환 작업량을 백엔드/eGovFrame 전환 범위에 포함하지 마라.
  
---

## 수행 작업

### 1. 프로젝트 구조 스캔

다음 항목을 확인하라.

- `pom.xml`
- `web.xml`
- `src/main/java`
- `src/main/resources`
- `src/main/webapp`
- Spring XML 설정 파일
- MyBatis/iBatis Mapper XML
- JSP 파일
- properties/yml 설정 파일

---

### 2. 전환 영향 지점 식별

아래 항목을 중심으로 전자정부프레임워크 4.3 전환 영향 지점을 찾아라.

#### Java 소스

- `javax.servlet.*`
- `javax.annotation.*`
- `javax.validation.*`
- `javax.websocket.*`
- `org.springframework.*`
- `egovframework.*`
- `EgovAbstractDAO`
- `EgovComAbstractDAO`
- `SqlMapClient`
- `JdbcTemplate`
- deprecated API 의심 지점
- Controller / Service / DAO / VO / Util 계층별 특이사항

#### XML 설정

- Spring bean 설정
- context namespace
- mvc namespace
- tx namespace
- aop namespace
- datasource 설정
- transaction 설정
- component-scan 설정
- servlet/filter/listener 설정
- web.xml 버전 및 schema

#### Mapper / SQL

- MyBatis mapper
- iBatis sqlMap
- namespace
- parameterClass / resultClass
- parameterType / resultType
- 동적 SQL
- resultMap

#### JSP / 화면

프론트엔드는 자동변환 대상이 아니므로 JSP/HTML/JavaScript/CSS 자체의 변환 필요성을 평가하지 않는다.

단, 서버 사이드 전환에 영향을 줄 수 있는 아래 항목은 식별만 한다.

- taglib 선언
- Spring form tag
- `form:form commandName`
- form action URL
- Controller mapping과 연결되는 URL
- include/import 지시어
- 서버 바인딩용 input name
- JSP에서 참조하는 model attribute

식별된 항목은 자동 변경 후보가 아니라 “수동 검토 필요”로 분류한다.

#### Maven / Dependency

- Spring 버전
- eGovFrame 버전
- Servlet/JSP/JSTL 관련 dependency
- MyBatis/iBatis 관련 dependency
- logging 관련 dependency
- build plugin
- Java source/target 버전

---

### 3. migration-policy 적합성 검증

현재 프로젝트 기준으로 migration-policy가 아래 항목을 충분히 다루는지 평가하라.

- 자동 변경 허용 규칙이 충분한가?
- 조건부 변경 규칙이 필요한 항목이 누락되었는가?
- 절대 변경 금지 항목이 명확한가?
- 수동 검토 필요 항목이 충분한가?
- 레이어별 정책이 충분한가?
- hallucination 방지 규칙이 충분한가?
- 출력 형식이 검증 가능하게 정의되어 있는가?

---

### 4. 정책 분류 기준

식별된 항목은 반드시 아래 4개 중 하나로 분류하라.

#### A. 자동 변경 허용

예:
- import 경로 단순 변경
- 명확한 패키지명 치환
- XML namespace/schema 버전 정리

#### B. 조건부 변경 허용

예:
- DAO 상속 구조 변경
- Spring XML bean → annotation 전환
- dependency 버전 변경
- web.xml schema 변경

#### C. 수동 검토 필요

예:
- transaction 경계 변경
- security/filter/interceptor 변경
- datasource 변경
- 배치/스케줄러 변경
- 외부 연계 설정 변경

#### D. 절대 변경 금지

예:
- 업무 로직 변경
- SQL 의미 변경
- 조건문 변경
- 계산식 변경
- 화면 항목명 임의 변경
- URL 임의 변경
- DB 컬럼명 임의 변경
- Mapper namespace 임의 변경

---

## 출력 형식

반드시 아래 형식으로만 답변하라.

```markdown
# Migration Policy 검증 결과

## 1. 검증 요약

- 검증 대상 프로젝트:
- 주요 기술 스택:
- 전환 난이도:
- 주요 위험 영역:

## 2. 프로젝트 구조 분석 결과

| 구분 | 확인 결과 | 근거 파일 |
|---|---|---|
| Maven |  |  |
| Java Source |  |  |
| Spring XML |  |  |
| Mapper XML |  |  |
| JSP |  |  |
| web.xml |  |  |

## 3. 전환 영향 지점 목록

| 영역 | 영향 지점 | 현재 사용 형태 | 예상 전환 방향 | 위험도 | 근거 파일 |
|---|---|---|---|---|---|

## 4. migration-policy 적합성 평가

| 정책 영역 | 평가 | 부족한 점 | 보완 필요 여부 |
|---|---|---|---|

## 5. 정책 보완 후보

| 우선순위 | 보완 항목 | 권장 정책 분류 | 보완 사유 | 근거 |
|---|---|---|---|---|

## 6. 자동 변경 허용 후보

| 항목 | 변경 전 | 변경 후 | 적용 조건 | 근거 |
|---|---|---|---|---|

## 7. 조건부 변경 후보

| 항목 | 조건 | 주의사항 | 근거 |
|---|---|---|---|

## 8. 수동 검토 필요 항목

| 항목 | 검토 사유 | 영향 범위 | 근거 |
|---|---|---|---|

## 9. 절대 변경 금지로 명시해야 할 항목

| 항목 | 금지 사유 | 예시 |
|---|---|---|

## 10. Hallucination 방지 규칙 보완

| 위험 유형 | 설명 | 방지 규칙 |
|---|---|---|

## 11. 최종 의견

- 현재 migration-policy 충분성:
- 즉시 보완해야 할 항목:
- 다음 단계 권장 작업: