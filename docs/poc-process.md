# 전자정부프레임워크 전환 PoC 절차

## 1. Global Policy Layer

- [ ] migration-policy 작성
- [ ] 공통 변환 원칙 정의
- [ ] 할루시네이션 방지 규칙 정의
- [ ] 소스 수정 허용/금지 범위 정의

## 2. Analysis Layer

- [ ] package-scan-analysis
- [ ] pom-analysis
- [ ] dependency-analysis
- [ ] dao-analysis
- [ ] sqlmap-analysis
- [ ] spring-context-analysis
- [ ] controller-analysis
- [ ] service-analysis
- [ ] batch-analysis
- [ ] compile-log-analysis

## 3. Conversion Layer

- [ ] DAO 변환
- [ ] SQLMap 변환
- [ ] Spring XML 변환
- [ ] Controller 변환
- [ ] Service 변환
- [ ] POM 변환

## 4. Validation Layer

- [ ] 변환 결과 검토
- [ ] 컴파일 오류 검토
- [ ] Diff 검토
- [ ] 재변환 필요사항 정리

## 5. Test Layer

- [ ] Maven compile
- [ ] 단위 실행 확인
- [ ] 주요 업무 흐름 테스트
- [ ] 반복 개선
