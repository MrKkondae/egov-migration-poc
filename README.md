# eGovFrame 3.x → 4.3 Migration PoC

## 프로젝트 개요

본 프로젝트는 전자정부 표준프레임워크(eGovFrame) 3.x 기반 시스템을 4.3 환경으로 전환하기 위한 PoC(Proof of Concept) 프로젝트이다.

주요 목표는 다음과 같다.

* eGovFrame 3.x → 4.3 전환 규칙 수립
* LLM(Qwen)을 활용한 소스 분석 자동화
* 전환 규칙(Mapping) 구축
* 소스 자동 변환(Conversion) 검증
* 컴파일 및 정합성 검증(Validation)
* 폐쇄망 환경 적용 가능성 검토

---

# 작업 절차

본 프로젝트는 다음 순서로 수행한다.

```text
Analysis
    ↓
Mapping
    ↓
Conversion
    ↓
Validation
```

| 단계         | 설명                    |
| ---------- | --------------------- |
| Analysis   | 기존 3.x 소스 및 설정 분석     |
| Mapping    | 3.x ↔ 4.3 구조 매핑 규칙 작성 |
| Conversion | 전환 규칙 기반 소스 변환        |
| Validation | 컴파일 및 정합성 검증          |

---

# 디렉토리 구조

```text
egov-migration-poc
│
├── docs
├── prompt
├── source
├── output
├── mapping
├── converted
├── scripts
└── tools
```

---

## docs

프로젝트 문서 및 전환 정책 관리

```text
docs
├── migration-policy.md
└── ...
```

주요 내용

* 전환 정책
* PoC 수행 절차
* Lessons Learned
* 분석 결과 정리

---

## prompt

LLM(Qwen) 프롬프트 관리

```text
prompt
├── 01-analysis
├── 02-mapping
├── 03-conversion
├── 04-validation
└── archive
```

### 01-analysis

기존 3.x 구조 분석

예)

```text
pom 분석
dependency 분석
DAO 분석
Service 분석
Controller 분석
SQLMap 분석
Spring XML 분석
```

### 02-mapping

3.x → 4.3 매핑 규칙 생성

예)

```text
Dependency Mapping
DAO Mapping
SQLMap Mapping
Spring XML Mapping
```

### 03-conversion

전환 수행 프롬프트

예)

```text
DAO Conversion
Service Conversion
Controller Conversion
SQLMap Conversion
```

### 04-validation

전환 결과 검증

예)

```text
Compile Validation
Dependency Validation
DAO Validation
```

### archive

과거 프롬프트 및 보관 자료

---

## source

원본 소스 및 기준 프로젝트

```text
source
├── 3.x
└── 4.3-boot
```

### 3.x

분석 대상 원본 시스템

### 4.3-boot

비교 및 전환 기준이 되는 4.3 Boot 프로젝트

---

## output

프롬프트 수행 결과 저장소

```text
output
├── 01-analysis
├── 02-mapping
├── 03-conversion
└── 04-validation
```

예)

```text
output/01-analysis/pom
output/01-analysis/dao

output/02-mapping/pom
output/02-mapping/dao

output/03-conversion/dao

output/04-validation/compile
```

주의

* output은 보고서/분석 결과 저장소이다.
* 실제 변환 소스는 저장하지 않는다.

---

## mapping

프로젝트 공통 전환 규칙 저장소

```text
mapping
├── pom
├── dao
├── service
├── controller
├── sqlmap
└── springxml
```

예)

```text
EgovAbstractDAO
→ EgovAbstractMapper

list()
→ selectList()

selectByPk()
→ selectOne()
```

특징

* 재사용 가능한 전환 규칙 저장
* Conversion 프롬프트의 참조 자료
* 프로젝트 전체 공통 지식베이스 역할 수행

---

## converted

실제 변환된 소스 저장소

```text
converted
├── src
└── resources
```

특징

* LLM 전환 결과 저장
* 컴파일 대상 소스 보관
* Validation 단계 입력 자료

---

## scripts

자동화 스크립트

예)

```text
Embedding 생성
문서 수집
검색 테스트
전처리
```

---

## tools

개발 도구 및 유틸리티

예)

```text
RAG 관련 도구
검색 도구
분석 도구
```

---

# 산출물 구분

| 구분        | 저장 위치                |
| --------- | -------------------- |
| 분석 결과     | output/01-analysis   |
| 매핑 결과     | output/02-mapping    |
| 전환 결과 보고서 | output/03-conversion |
| 검증 결과     | output/04-validation |
| 전환 규칙     | mapping              |
| 실제 변환 소스  | converted            |
| 원본 소스     | source               |

---

# 운영 원칙

1. Analysis 결과 없이 Conversion 수행 금지
2. Mapping 규칙 없이 Conversion 수행 금지
3. Conversion 결과는 반드시 Validation 수행
4. 전환 규칙은 mapping 디렉토리에 누적 관리
5. Prompt 결과와 실제 변환 소스를 분리 관리
6. 모든 산출물은 단계별(output)로 관리
