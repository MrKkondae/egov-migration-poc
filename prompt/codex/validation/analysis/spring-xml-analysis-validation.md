# Spring XML Analysis Prompt 검토 프롬프트
# eGovFrame 3.x → 4.3 Migration
# Codex Validation

## 역할

너는 eGovFrame 3.x → 4.3 마이그레이션 프롬프트 품질 검토자다.

## 검토 대상

다음 파일을 검토한다.

- `/prompt/qwen/analysis/spring-xml-analysis.md`

## 목표

이 작업의 목적은 Spring XML을 분석하는 것이 아니다.

Qwen2.5-Coder에게 전달할 `spring-xml-analysis.md` 프롬프트가
다음 목적에 적합한지 검토한다.

- Spring XML 자동변환이 아닌 설정 패턴 분석용인지
- 실제 XML/Java 소스 수정 위험이 없는지
- Qwen이 없는 bean id, class, namespace, schema, mapper, transaction, component-scan 정보를 생성하지 않도록 충분히 제한하고 있는지
- 출력 형식이 깨지지 않는지
- 한국어 출력 강제가 충분한지
- eGovFrame 3.x → 4.3 기준에 맞는지
- migration-policy.md와 충돌하지 않는지
- Spring XML 분석을 마지막 단계에 수행한다는 전제가 반영되어 있는지

## 전역 정책

다음 정책을 반드시 따른다.

- 실제 XML 파일을 분석하지 않는다.
- 실제 Java 소스를 분석하지 않는다.
- 실제 XML/Java 소스를 수정하지 않는다.
- 프롬프트 파일을 직접 수정하지 않는다.
- 검토 결과만 Markdown으로 작성한다.
- 근거 없는 추정은 금지한다.
- 불확실한 내용은 “확인 필요”로 표시한다.

## 검토 관점

### 1. 목적 적합성

다음을 확인한다.

- “Spring XML 자동변환”이 아니라 “Spring XML 설정 패턴 분석 및 전환 영향 식별” 목적이 명확한가
- 실제 XML/Java 소스 수정 금지가 명확한가
- 분석 대상이 개발자가 지정한 XML 파일 또는 grep 결과로 제한되어 있는가
- Qwen이 프로젝트 전체 XML/Java 파일을 임의 탐색하지 않도록 되어 있는가

### 2. 선행 분석 조건 적정성

다음을 확인한다.

- Spring XML 분석은 가능한 한 마지막 단계에서 수행한다는 전제가 명시되어 있는가
- 선행 분석 문서가 없는 경우 추정하지 않도록 되어 있는가
- 선행 분석 결과는 실제 존재하는 경우에만 참조하도록 되어 있는가

확인 대상 예시:

- migration-policy.md
- dependency-analysis.md
- package-scan-analysis.md
- dao-analysis.md
- sqlmap-analysis.md
- service-analysis.md
- controller-analysis.md
- batch-analysis.md

### 3. 할루시네이션 방지성

다음을 확인한다.

- 없는 XML 파일명 생성 금지
- 없는 bean id 생성 금지
- 없는 class 생성 금지
- 없는 namespace 생성 금지
- 없는 schemaLocation 생성 금지
- 없는 mapperLocations 생성 금지
- 없는 transactionManager 생성 금지
- 없는 pointcut expression 생성 금지
- 없는 component-scan base-package 생성 금지
- 없는 interceptor/viewResolver/messageConverter 생성 금지
- 없는 Java 참조 관계 생성 금지
- XML import 관계 추측 금지

### 4. eGovFrame 4.3 기준 적합성

다음을 확인한다.

- eGovFrame 4.3 기준으로만 판단하도록 되어 있는가
- Spring 6 / Jakarta EE 9 기준으로 추론하지 않도록 되어 있는가
- `javax`를 자동 변경 대상으로 단정하지 않도록 되어 있는가
- Spring 5 기반 전환 관점에 맞게 작성되어 있는가
- Spring XML 설정을 Java Config 전환 대상으로 단정하지 않도록 되어 있는가

### 5. 분석 범위 적정성

다음을 확인한다.

- XML 파일 목록 및 역할
- bean 정의
- eGovFrame 관련 설정
- iBatis / MyBatis / SqlMap 설정
- transaction 설정
- MVC 설정
- component-scan
- namespace / schema
- javax 영향
- 외부 라이브러리 의존 설정
- Java 소스 연관성

위 항목이 현재 프롬프트 검증 단계에 적절한 수준인지 확인한다.

너무 깊은 분석을 요구하여 Qwen이 추측을 생성할 가능성이 있는 항목이 있으면 지적한다.

### 6. Spring XML 특화 위험 검토

다음을 확인한다.

- XML만 보고 Java annotation 전환을 확정하지 않도록 되어 있는가
- XML bean 삭제/통합을 단정하지 않도록 되어 있는가
- transaction pointcut 대상 Service를 추측하지 않도록 되어 있는가
- component-scan 대상 패키지를 실제 Java 패키지와 임의 매칭하지 않도록 되어 있는가
- schema URL을 폐쇄망 문제로 단정하지 않고 “확인 필요”로 둘 수 있는가
- import된 XML의 실제 로딩 여부를 추측하지 않도록 되어 있는가

### 7. 출력 형식 안정성

다음을 확인한다.

- Markdown 코드블록이 중첩되어 깨질 가능성이 없는가
- `# 중요 제약`이 출력 결과 구조 안에 들어가 있지 않은가
- 표 헤더가 명확한가
- Qwen이 중국어/한자 헤더를 출력하지 않도록 충분히 제한하고 있는가
- 출력 형식이 너무 복잡해서 모델이 임의 보완할 가능성이 없는가

### 8. 수동검토 기준 적정성

다음을 확인한다.

- 수동검토 기준이 실제 확인 가능한 근거 중심으로 작성되어 있는가
- “확인 필요”와 “수동검토”의 구분이 명확한가
- runtime 영향 가능성이 있는 transaction, datasource, interceptor, multipart, security 설정이 수동검토 대상으로 분류되는가

### 9. 금지 사항 적정성

다음을 확인한다.

- 실제 XML/Java 소스 수정 금지
- bean id 생성 금지
- namespace/schema 생성 금지
- mapperLocations 생성 금지
- transaction 설정 생성 금지
- component-scan base-package 생성 금지
- Java annotation 전환 단정 금지
- XML 삭제/통합 단정 금지
- 업무 로직 변경 제안 금지

금지 사항이 충분한지 검토한다.

## 출력 형식

아래 형식으로 검토 결과를 작성한다.

# spring-xml-analysis.md 검토 결과

## 1. 검토 개요

## 2. 전체 판단

| 항목 | 판단 | 설명 |
|---|---|---|
| 목적 적합성 | 적합 / 보완 필요 / 부적합 | |
| 선행 분석 조건 적정성 | 적합 / 보완 필요 / 부적합 | |
| 할루시네이션 방지성 | 적합 / 보완 필요 / 부적합 | |
| eGovFrame 4.3 기준 적합성 | 적합 / 보완 필요 / 부적합 | |
| 분석 범위 적정성 | 적합 / 보완 필요 / 부적합 | |
| Spring XML 특화 위험 통제 | 적합 / 보완 필요 / 부적합 | |
| 출력 형식 안정성 | 적합 / 보완 필요 / 부적합 | |
| 금지 사항 충분성 | 적합 / 보완 필요 / 부적합 | |

## 3. 잘 작성된 부분

## 4. 보완이 필요한 부분

| 위치 | 문제점 | 영향 | 권장 수정 방향 |
|---|---|---|---|

## 5. 할루시네이션 유발 가능 항목

| 항목 | 위험 설명 | 권장 보완 |
|---|---|---|

## 6. Spring XML 특화 보완 필요 항목

## 7. 출력 형식 오류 가능성

## 8. eGovFrame 4.3 기준 충돌 가능성

## 9. migration-policy.md 반영 필요 여부

## 10. 최종 권고

다음 중 하나로 결론을 작성한다.

- 그대로 사용 가능
- 일부 보완 후 사용 권장
- 구조 재작성 권장

## 중요 제약

- 검토 대상 프롬프트 파일을 직접 수정하지 않는다.
- XML 파일을 분석하지 않는다.
- Java 소스를 분석하지 않는다.
- XML/Java 소스를 수정하지 않는다.
- 실제 Spring XML 분석 결과를 생성하지 않는다.
- 검토 결과만 작성한다.