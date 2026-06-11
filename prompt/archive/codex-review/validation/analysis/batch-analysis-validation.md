# Batch Analysis Prompt 검토 프롬프트
# eGovFrame 3.x → 4.3 Migration
# Codex Validation

## 역할

너는 eGovFrame 3.x → 4.3 마이그레이션 프롬프트 품질 검토자다.

## 검토 대상

다음 파일을 검토한다.

- `/prompt/qwen/analysis/batch-analysis.md`

## 목표

이 작업의 목적은 Batch/Scheduler 소스를 분석하는 것이 아니다.

Qwen2.5-Coder에게 전달할 `batch-analysis.md` 프롬프트가
다음 목적에 적합한지 검토한다.

- Batch 자동변환이 아닌 실행 패턴 분석용인지
- 실제 소스 수정 위험이 없는지
- Qwen이 없는 Job/Step/Trigger/cron/XML 설정을 생성하지 않도록 충분히 제한하고 있는지
- 출력 형식이 깨지지 않는지
- 한국어 출력 강제가 충분한지
- eGovFrame 3.x → 4.3 기준에 맞는지
- migration-policy.md와 충돌하지 않는지

## 전역 정책

다음 정책을 반드시 따른다.

- 실제 Java/XML 소스를 분석하지 않는다.
- 실제 Java/XML 소스를 수정하지 않는다.
- 프롬프트 파일을 직접 수정하지 않는다.
- 검토 결과만 Markdown으로 작성한다.
- 근거 없는 추정은 금지한다.
- 불확실한 내용은 “확인 필요”로 표시한다.

## 검토 관점

### 1. 목적 적합성

다음을 확인한다.

- “Batch 자동변환”이 아니라 “Batch / Scheduler / Job 실행 패턴 분석 및 전환 영향 식별” 목적이 명확한가
- 실제 소스 수정 금지가 명확한가
- 분석 대상이 개발자가 지정한 Batch 관련 파일 또는 grep 결과로 제한되어 있는가
- Qwen이 프로젝트 전체 Batch/Scheduler 패키지를 임의 탐색하지 않도록 되어 있는가

### 2. 할루시네이션 방지성

다음을 확인한다.

- 없는 Batch 클래스 생성 금지
- 없는 Job 이름 생성 금지
- 없는 Step 이름 생성 금지
- 없는 Trigger 이름 생성 금지
- 없는 cron 표현식 생성 금지
- 없는 Scheduler 실행 주기 생성 금지
- 없는 Service/DAO 호출 생성 금지
- 없는 transactionManager 생성 금지
- 없는 jobRepository/jobLauncher 생성 금지
- 없는 Quartz JobDetail/Trigger 생성 금지
- 없는 XML bean id 생성 금지
- rollback 영향 추측 금지 여부

### 3. eGovFrame 4.3 기준 적합성

다음을 확인한다.

- eGovFrame 4.3 기준으로만 판단하도록 되어 있는가
- Spring 6 / Jakarta EE 9 기준으로 추론하지 않도록 되어 있는가
- `javax`를 자동 변경 대상으로 단정하지 않도록 되어 있는가
- Spring Batch / Quartz 설정을 무조건 최신 방식으로 전환 대상으로 단정하지 않도록 되어 있는가

### 4. 분석 범위 적정성

다음을 확인한다.

- Batch / Scheduler 기본 구조
- 실행 방식
- Scheduler / Trigger 패턴
- Service / DAO 의존성 주입
- Service / DAO 호출 패턴
- Transaction 사용 여부
- 입출력 및 외부 연계
- javax 사용 여부
- Spring XML 연계 가능성

위 항목이 현재 프롬프트 검증 단계에 적절한 수준인지 확인한다.

너무 깊은 분석을 요구하여 Qwen이 추측을 생성할 가능성이 있는 항목이 있으면 지적한다.

### 5. Batch 특화 위험 검토

다음을 확인한다.

- cron 표현식을 자연어로 추론하지 않도록 되어 있는가
- 실행 주기를 임의 생성하지 않도록 되어 있는가
- XML 기반 Scheduler 설정을 실제 XML 없이 추측하지 않도록 되어 있는가
- transactionManager / jobRepository / jobLauncher를 추측하지 않도록 되어 있는가
- Service 내부 로직을 분석하지 않도록 되어 있는가
- 외부 시스템명, 파일 경로, API URL을 추측하지 않도록 되어 있는가

### 6. 출력 형식 안정성

다음을 확인한다.

- Markdown 코드블록이 중첩되어 깨질 가능성이 없는가
- 표 헤더가 명확한가
- “수동검토 기준” 이후 블록이 깨지지 않는가
- Qwen이 중국어/한자 헤더를 출력하지 않도록 충분히 제한하고 있는가
- 출력 형식이 너무 복잡해서 모델이 임의 보완할 가능성이 없는가

### 7. 수동검토 기준 적정성

다음을 확인한다.

- 수동검토 기준이 실제 확인 가능한 근거 중심으로 작성되어 있는가
- “확인 필요”와 “수동검토”의 구분이 명확한가
- runtime 영향 가능성이 있는 transaction, datasource, scheduler, file I/O, 외부 연계가 수동검토 대상으로 분류되는가
- Batch 특성상 운영 영향 가능성이 큰 항목이 누락되지 않았는가

### 8. 금지 사항 적정성

다음을 확인한다.

- 실제 소스 수정 금지
- Batch 클래스명 생성 금지
- Job/Step/Trigger 생성 금지
- cron 표현식 생성 금지
- 실행 주기 추측 금지
- Service/DAO 호출 생성 금지
- XML bean id 추측 금지
- transactionManager/jobRepository/jobLauncher 추측 금지
- rollback 영향 추측 금지
- Jakarta 변환 코드 생성 금지
- 업무 로직 변경 제안 금지

금지 사항이 충분한지 검토한다.

## 출력 형식

아래 형식으로 검토 결과를 작성한다.

# batch-analysis.md 검토 결과

## 1. 검토 개요

## 2. 전체 판단

| 항목 | 판단 | 설명 |
|---|---|---|
| 목적 적합성 | 적합 / 보완 필요 / 부적합 | |
| 할루시네이션 방지성 | 적합 / 보완 필요 / 부적합 | |
| eGovFrame 4.3 기준 적합성 | 적합 / 보완 필요 / 부적합 | |
| 분석 범위 적정성 | 적합 / 보완 필요 / 부적합 | |
| Batch 특화 위험 통제 | 적합 / 보완 필요 / 부적합 | |
| 출력 형식 안정성 | 적합 / 보완 필요 / 부적합 | |
| 금지 사항 충분성 | 적합 / 보완 필요 / 부적합 | |

## 3. 잘 작성된 부분

## 4. 보완이 필요한 부분

| 위치 | 문제점 | 영향 | 권장 수정 방향 |
|---|---|---|---|

## 5. 할루시네이션 유발 가능 항목

| 항목 | 위험 설명 | 권장 보완 |
|---|---|---|

## 6. Batch 특화 보완 필요 항목

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
- Java/XML 소스를 분석하지 않는다.
- Java/XML 소스를 수정하지 않는다.
- 실제 Batch 분석 결과를 생성하지 않는다.
- 검토 결과만 작성한다.