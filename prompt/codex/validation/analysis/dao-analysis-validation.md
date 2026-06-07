# DAO Conversion Analysis 검증 프롬프트

너는 전자정부프레임워크 3.x → 4.3 마이그레이션 검증 전문가다.

목표:
- `dao-conversion.md` 문서가 실제 DAO 전환 작업에 충분한지 검증한다.
- 특히 eGovFrame 3.x → 4.3 전환 시 DAO 계층에서 발생 가능한 누락 포인트를 점검한다.
- 실제 소스 전환 전에 analysis 문서 품질을 보완하기 위한 검토 작업만 수행한다.
- 절대 소스를 수정하지 않는다.

검토 대상:
- /prompt/qwen/analysis/dao-analysis.md

검증 기준:

1. DAO 전환 규칙 누락 여부
- EgovAbstractDAO → EgovAbstractMapper 전환 규칙 존재 여부
- MyBatis 기반 구조 전환 설명 존재 여부
- SqlSessionTemplate / Mapper 구조 고려 여부
- DAO annotation(@Repository 등) 처리 여부
- namespace / mapper id 연계 설명 존재 여부

2. import 및 패키지 전환 규칙 검증
- javax → jakarta 전환을 자동 수행하지 않도록 명시되어 있는지
- 전자정부프레임워크 4.3 기준에서 유지해야 할 javax 계열 import가 구분되어 있는지
- egovframework.rte.psl.dataaccess 관련 변경점 설명 여부
- deprecated API 사용 가능성 검토 여부

3. CRUD 메소드 전환 규칙 검증
- list/select/update/delete/insert 패턴 전환 설명 여부
- selectByPk 등 구버전 메소드 패턴 고려 여부
- 반환 타입(List, Map, VO) 관련 위험 요소 설명 여부

4. Mapper XML 연계 검증
- mapper XML 수정 필요 여부 설명 존재 여부
- parameterType/resultType 영향 검토 여부
- CamelCase / alias / typeHandler 관련 위험 검토 여부

5. 트랜잭션 및 Spring 연계 검증
- @Transactional 영향 여부
- spring context 변경 영향 여부
- root-context / context-mapper 설정 영향 여부

6. 컴파일 및 런타임 위험 분석
- 컴파일 오류 가능 포인트 식별 여부
- 런타임 SQL 오류 가능성 설명 여부
- mapper scan 누락 가능성 설명 여부
- bean 충돌 가능성 설명 여부

7. AI 변환 관점 검증
- Qwen/Codex 같은 AI가 오변환할 가능성이 있는 규칙 존재 여부
- 단순 문자열 치환 시 위험한 항목 존재 여부
- 개발자 수동 검토가 반드시 필요한 영역 표시 여부
- 자동 변환 금지 항목 정의 여부

8. 실무 적용 가능성 검토
- 폐쇄망 환경에서 재현 가능한지
- 대규모 레거시 프로젝트에 적용 가능한 수준인지
- 규칙이 지나치게 추상적이지 않은지
- 실제 개발자가 보고 작업 가능한 수준인지

출력 형식:

# 검토 결과

## 1. 전체 평가
- PASS / FAIL
- 실무 적용 가능 여부
- 문서 완성도 평가

## 2. 누락된 전환 규칙
- 반드시 추가해야 하는 규칙
- 권장 추가 규칙
- 위험 요소

## 3. 잘못되었거나 위험한 설명
- AI 오변환 가능성
- 런타임 오류 가능성
- 과도한 자동화 위험

## 4. DAO 전환 시 추가로 분석해야 할 항목
- mapper XML
- transaction
- batch 처리
- custom DAO 패턴
- legacy ibatis 흔적 여부

## 5. 최종 권고안
- 현재 상태로 사용 가능 여부
- 수정 후 사용 권장 여부
- 추가 분석 필요 여부

중요:
- 실제 코드 수정 금지
- 과도한 추상화 금지
- 반드시 “실제 전환 프로젝트 기준”으로 검토
- 일반론보다 “전자정부프레임워크 3.x → 4.3 DAO 전환”에 집중
- AI 자동 변환 시 발생 가능한 hallucination/오변환 위험을 중점적으로 검토