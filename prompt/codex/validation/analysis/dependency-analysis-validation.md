
너는 전자정부프레임워크 3.x → 4.x 전환을 위한 의존성 분석 프롬프트 품질 검토 전문가다.

## 검토 대상

- 파일 경로: `prompt/qwen/analysis/dependency-analysis.md`

## 검토 목적

`dependency-analysis.md`는 Qwen이 프로젝트의 Maven/Gradle 의존성, 라이브러리, 프레임워크 버전, 전환 위험 요소를 분석하기 위한 프롬프트다.

이 프롬프트가 실제 전자정부프레임워크 3.x → 4.x 전환 분석에 충분한지 검토하라.

단, 이번 작업에서는 절대 소스나 프롬프트 파일을 수정하지 않는다.  
검토 결과와 보완 제안만 작성한다.

## 검토 관점

다음 항목을 기준으로 면밀히 검토하라.

### 1. 분석 범위 적정성

- Maven `pom.xml`, Gradle `build.gradle`, `settings.gradle` 분석 범위가 명확한가?
- parent POM, dependencyManagement, pluginManagement, profile, module 구조 분석이 포함되어 있는가?
- 직접 의존성과 전이 의존성의 구분이 명확한가?
- scope별 의존성 구분이 가능한가?
  - compile
  - provided
  - runtime
  - test
  - optional

### 2. 전자정부프레임워크 전환 관점

- `egovframework` → `org.egovframe` 전환 기준이 포함되어 있는가?
- 전자정부프레임워크 버전 확인 기준이 명확한가?
- Spring, Spring MVC, Spring Security, MyBatis/iBatis, Servlet API, JSP/JSTL 등 주요 연계 라이브러리의 전환 영향 분석이 가능한가?
- eGovFrame 4.x 적용 시 Java, Servlet, Jakarta, WAS 호환성 검토 기준이 포함되어 있는가?

### 3. javax / jakarta 전환 위험 분석

- `javax.*` 계열 의존성 식별 기준이 포함되어 있는가?
- `jakarta.*` 계열 의존성 식별 기준이 포함되어 있는가?
- `javax`와 `jakarta`가 혼재될 경우 위험으로 판단하도록 되어 있는가?
- 단순 문자열 치환이 아닌 라이브러리 버전 호환성 관점의 판단 기준이 있는가?

### 4. 중복 / 충돌 / 구버전 라이브러리 분석

- 동일 라이브러리의 다중 버전 충돌 분석이 가능한가?
- Spring 계열 라이브러리 버전 불일치 분석이 가능한가?
- logging 계열 충돌 분석 기준이 포함되어 있는가?
  - log4j
  - log4j2
  - slf4j
  - commons-logging
  - logback
- XML 파서, JSON, Apache Commons, DB Driver, 보안 라이브러리 등 공통 라이브러리 충돌 가능성을 점검하는가?
- 오래된 취약 라이브러리 식별 기준이 있는가?

### 5. DB / ORM / SQL Mapper 관련 의존성

- iBatis, MyBatis, MyBatis-Spring 의존성 구분 기준이 있는가?
- 전자정부프레임워크 3.x에서 사용하던 DAO / SqlMap / Mapper 구조와 연결해 분석할 수 있는가?
- JDBC Driver, connection pool, transaction 관련 라이브러리 분석 기준이 포함되어 있는가?

### 6. WAS / Servlet / JSP 관련 의존성

- servlet-api, jsp-api, jstl, taglibs 등의 provided/runtime 구분 기준이 있는가?
- Tomcat, WebLogic, JEUS 등 WAS 제공 라이브러리와 애플리케이션 포함 라이브러리의 충돌 가능성을 분석하는가?
- 전자정부프레임워크 4.x 적용 시 Servlet 스펙 버전 차이를 고려하는가?

### 7. 산출물 품질

- 분석 결과 산출물 형식이 명확한가?
- 위험도 분류 기준이 있는가?
  - 높음
  - 중간
  - 낮음
- 각 의존성에 대해 다음 항목을 정리하도록 되어 있는가?
  - groupId
  - artifactId
  - version
  - scope
  - 사용 목적 추정
  - 전환 영향도
  - 위험도
  - 조치 필요 여부
  - 권장 조치
- Qwen이 추측하지 않고 근거 기반으로 작성하도록 통제되어 있는가?

### 8. 할루시네이션 방지

- 실제 파일에 존재하지 않는 dependency를 만들어내지 않도록 명시되어 있는가?
- 버전 정보를 추정하지 않도록 되어 있는가?
- 확인 불가 항목은 “확인 필요”로 표시하도록 되어 있는가?
- 소스 수정, dependency 수정, 버전 변경 제안 적용을 금지하고 있는가?
- 분석과 변경 작업이 명확히 분리되어 있는가?

### 9. 다른 분석 프롬프트와의 연계성

- `pom-analysis.md`, `package-scan-analysis.md`, `sqlmap-analysis.md`, `dao-analysis.md` 등 다른 분석 프롬프트와 역할이 중복되거나 충돌하지 않는가?
- dependency-analysis의 역할이 “의존성 및 라이브러리 전환 위험 분석”으로 명확히 한정되어 있는가?
- Java 소스 내부 import 분석과 POM/Gradle dependency 분석의 책임 경계가 분명한가?

## 출력 형식

다음 형식으로 검토 결과를 작성하라.

# dependency-analysis.md 검토 결과

## 1. 총평

현재 프롬프트의 장점과 전체적인 완성도를 요약한다.

## 2. 보완 필요 사항

아래 표 형식으로 작성한다.

| 구분 | 현재 문제점 | 보완 필요 내용 | 우선순위 |
|---|---|---|---|
| 분석 범위 |  |  | 높음/중간/낮음 |
| 전환 기준 |  |  | 높음/중간/낮음 |
| javax/jakarta |  |  | 높음/중간/낮음 |
| 의존성 충돌 |  |  | 높음/중간/낮음 |
| 산출물 |  |  | 높음/중간/낮음 |
| 할루시네이션 방지 |  |  | 높음/중간/낮음 |
| 타 프롬프트 연계 |  |  | 높음/중간/낮음 |

## 3. 반드시 추가해야 할 내용

`dependency-analysis.md`에 반드시 반영해야 할 내용을 구체적으로 작성한다.

## 4. 제외하거나 약화해도 되는 내용

dependency-analysis의 책임 범위를 벗어나는 내용이 있다면 정리한다.

## 5. 권장 산출물 구조

Qwen이 dependency 분석 후 작성해야 할 결과물 목차를 제안한다.

예시:

```markdown
# Dependency Analysis Result

## 1. 분석 대상 파일

## 2. 전체 의존성 요약

## 3. eGovFrame 관련 의존성

## 4. Spring 계열 의존성

## 5. Servlet / JSP / JSTL / Jakarta 관련 의존성

## 6. DB / ORM / SQL Mapper 관련 의존성

## 7. Logging 관련 의존성

## 8. 보안 / 암호화 관련 의존성

## 9. 중복 및 버전 충돌 가능성

## 10. 전환 위험도 요약

## 11. 확인 필요 사항

## 12. 권장 조치

# 6. 최종 의견

현재 dependency-analysis.md를 그대로 사용해도 되는지, 보완 후 사용해야 하는지 판단하라.

판단은 다음 중 하나로 작성한다.

- 사용 가능
- 일부 보완 후 사용 권장
- 구조 보완 후 재검토 필요