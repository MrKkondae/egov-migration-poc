# pom-analysis.md 검토 프롬프트

너는 전자정부프레임워크 3.x → 4.3/4.5 전환 검증 전문가이며,
Java/Spring/Maven 기반 레거시 시스템 분석 경험이 풍부한 아키텍트다.

아래 첨부된 `pom-analysis.md` 문서를 검토하여,
실제 레거시 전환 프로젝트에서 사용할 수 있는 수준인지 품질 관점에서 분석해라.

---

## 검토 대상

- 경로:
  `/prompt/qwen/analysis/pom-analysis.md`

- 목적:
  Maven pom.xml 기반 의존성/플러그인/빌드 환경 분석용 프롬프트 검증

---

## 검토 목표

다음 항목을 중점적으로 검토한다.

### 1. 분석 범위 적절성

다음 항목들이 충분히 포함되어 있는지 검토:

- parent/child pom 구조
- dependencyManagement
- plugins/build 설정
- profiles
- repositories/pluginRepositories
- Java version/source/target
- Spring/eGovFrame 버전
- javax → jakarta 영향 가능성
- iBatis/MyBatis/JPA/Hibernate 혼재 여부
- servlet/jsp/tomcat 관련 라이브러리
- logging framework(log4j/slf4j/logback 등)
- deprecated/legacy 라이브러리
- 중복 dependency
- version 누락
- SNAPSHOT/local dependency
- system scope 사용 여부
- proprietary/vendor library 사용 가능성
- WAR/JAR packaging 구조
- multi-module 가능성

---

### 2. 전환 관점 위험 분석 적절성

다음 위험 요소를 충분히 탐지할 수 있는지 검토:

- eGovFrame 4.x 비호환 라이브러리
- Java 8 → Java 17 이상 전환 시 위험
- jakarta namespace 영향
- servlet container 의존성
- 구버전 Spring 충돌 가능성
- commons-logging/log4j1 등 레거시 의존성
- Maven plugin 버전 호환성 문제
- Oracle JDBC/상용 라이브러리 의존성
- 로컬 jar 직접 참조 구조
- framework 혼재 구조(Spring + Struts 등)

---

### 3. Hallucination 방지 수준 검토

다음 항목이 충분한지 검토:

- pom.xml에 실제 존재하는 내용만 분석하도록 제한되어 있는가
- 추측 기반 판단 금지 규칙이 충분한가
- dependency 이름만 보고 기술스택을 단정하지 않도록 되어 있는가
- 실제 version/configuration 기준으로 판단하도록 유도하는가
- source 수정 금지 원칙이 명확한가

---

### 4. 출력 구조 품질 검토

다음 사항을 검토:

- 결과 구조가 실제 프로젝트 분석 보고서 형태로 적절한가
- 위험도 구분(상/중/하)이 필요한가
- 표 구조가 충분히 실무적인가
- 후속 analysis prompt와 연계 가능한 구조인가
- conversion prompt 입력자료로 사용 가능한 수준인가

---

### 5. 누락된 분석 항목 검토

실제 전자정부프레임워크 전환 프로젝트 경험 기준으로,
pom 분석 시 추가되어야 할 항목이 있다면 상세히 제안해라.

특히 아래 관점 포함:

- 폐쇄망 환경
- 온프레미스 환경
- 상용 WAS(WebLogic/JEUS)
- CI/CD 환경
- 형상관리 연계
- 사내 공통 framework/library
- encoding/build 옵션
- annotation processor/lombok/mapstruct 등

---

## 매우 중요한 검토 규칙

- 반드시 실제 전환 프로젝트 기준으로 검토한다.
- 단순 Maven 일반론 수준으로 답변하지 않는다.
- 실제 SI/공공 프로젝트 리스크 중심으로 검토한다.
- 추상적 표현보다 실제 보완 가능한 규칙 단위로 설명한다.
- "좋다/부족하다" 수준이 아니라,
  왜 위험한지와 어떻게 보완해야 하는지 구체적으로 설명한다.

---

## 출력 형식

반드시 아래 형식으로 답변:

# pom-analysis.md 검토 결과

## 1. 총평

(문서 전체 품질 평가)

---

## 2. 잘된 점

- ...
- ...

---

## 3. 보완 필요 사항

### 3-1. [제목]

문제점:
- ...

위험성:
- ...

보완 방법:
- ...

예시:
```md
(실제 추가 가능한 규칙 예시)

## 4. 추가 권장 분석 항목

- ...
- ...

## 5. 최종 평가
- 실무 사용 가능 여부
- 추가 보완 필요 수준
- hallucination 방어 수준 평가
- 실제 전환 프로젝트 적용 가능성 평가