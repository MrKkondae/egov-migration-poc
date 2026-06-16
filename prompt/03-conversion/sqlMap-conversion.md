전자정부프레임워크 3.1 → 4.3 전환 PoC 작업 중이다.

방금 생성한 결과는 그대로 사용할 수 없다.  
아래 문제를 반드시 수정하여 같은 파일을 다시 변환하라.

대상 파일:  
`source/cf-egovboard-war/hello-egov-board/src/main/resources/egovframework/sqlmap/com/sym/cal/EgovRestdeManage_SQL_Oracle.xml`

생성 대상:  
`converted/cf-egovboard-war/hello-egov-board/src/main/resources/egovframework/sqlmap/com/sym/cal/EgovRestdeManage_SQL_Oracle.xml`

## 이번 재작업의 목적
- 이전 답변의 형식 오류와 XML 변환 오류를 수정한다.
- SQL 의미를 바꾸지 않고 MyBatis mapper XML로 다시 출력한다.
- 이번에는 반드시 “바로 저장 가능한 XML 전체 내용”을 일반 텍스트로 출력한다.

## 가장 중요한 오류 요약
1. JSON 형식으로 답변했다.
- `create_new_file` 같은 JSON wrapper는 금지한다.
- 이번에는 JSON, function call, tool call 형식으로 출력하지 마라.
- `read_file`, `open_file`, `load_file`, `fetch_file` 같은 파일 읽기 요청 형식도 금지한다.
- 입력 파일을 다시 읽겠다는 준비 단계 응답을 하지 말고, 최종 산출물만 바로 출력하라.

2. 동적 SQL에서 `prepend="AND"` 의미를 잃어버렸다.
- `<isEqual prepend="AND" ...>` 를 `<if>` 로 바꾸면서 `AND` 가 빠진 SQL을 만들었다.
- 이건 SQL 문법 오류를 만든다.
- 반드시 `AND` 를 보존해야 한다.

3. `<if test="...">` 속성 문자열이 깨졌다.
- `test` 속성의 따옴표가 닫히지 않은 잘못된 XML을 만들면 안 된다.
- 모든 `<if test="...">` 는 완전한 XML 문법이어야 한다.

4. 실제로 없는 `$param$` 위험 TODO를 넣었다.
- 원본 SQLMap 본문에 `$param$` 패턴이 없으면 `$param$` 관련 TODO를 추가하지 마라.
- 주석 텍스트에 `$->#변경` 이 있다고 해서 `$param$` 사용으로 판단하지 마라.

5. alias 관련 TODO를 과도하게 넣었다.
- 이 파일 안의 `<typeAlias>` 선언만으로 확인 가능한 alias는 불필요한 TODO 없이 FQCN으로 치환하라.
- 단, `<typeAlias>` 태그 자체는 최종 XML에 남기지 마라.

## 반드시 지킬 출력 형식
- JSON 금지.
- 반드시 아래 순서로 일반 텍스트로 출력한다.
- 최종 답변은 순수한 일반 텍스트여야 하며, JSON 객체, JSON 배열, 함수 호출, tool call, `create_new_file` 형식으로 시작하면 오답으로 간주한다.
- `read_file`, `open_file`, `load_file`, `fetch_file` 같은 파일 읽기 요청 형식으로 시작해도 오답으로 간주한다.
- 최종 답변 전에 파일을 읽겠다는 요청, 준비 단계 설명, 도구 호출 제안, 추가 입력 요청을 출력하지 마라.

1. 생성 대상 경로
2. 변환된 전체 XML
3. 수동검토 필요 항목 목록

### 출력 예시 형식
생성 대상 경로:
`converted/.../EgovRestdeManage_SQL_Oracle.xml`

변환 결과 XML:
`<?xml version="1.0" encoding="UTF-8"?>`
로 시작하는 완전한 XML 전체를 출력한다.

수동검토 필요 항목:
- 실제 발견 항목 1
- 실제 발견 항목 2

또는

수동검토 필요 항목:
- 없음

### 수동검토 필요 항목 작성 규칙
- `수동검토 필요 항목` 섹션은 반드시 출력한다.
- 하지만 체크리스트를 관성적으로 나열하지 마라.
- 현재 파일에서 실제로 발견된 항목만 작성한다.
- 실제 발견된 수동검토 필요 항목이 하나도 없으면 반드시 `없음` 이라고 작성한다.
- `$param$` 가 없으면 `$param$ 사용 여부` 를 쓰지 마라.
- `<selectKey>` 가 없으면 `selectKey 사용 여부` 를 쓰지 마라.
- 동적 SQL 의미 보존 문제가 해결되었으면 `동적 SQL 의미 보존 여부` 를 쓰지 마라.
- alias를 XML 내부 근거만으로 FQCN으로 확정했다면 `alias/FQCN 확정 여부` 를 쓰지 마라.

## 이번 재작업의 상세 규칙

### 1. XML 문서 형식
- 최종 결과는 반드시 XML declaration으로 시작한다.
- 예: `<?xml version="1.0" encoding="UTF-8"?>`
- `<!DOCTYPE sqlMap ...>` 는 제거한다.
- 루트는 반드시 `<mapper namespace="RestdeManage">` 로 출력한다.
- 최종 XML 안에 `<sqlMap` 이 남아 있으면 안 된다.

### 2. namespace / statement id 유지
- `namespace="RestdeManage"` 는 그대로 유지한다.
- 모든 statement id는 원본 그대로 유지한다.
- 대소문자도 바꾸지 않는다.

### 3. parameter placeholder
- 모든 `#param#` 를 `#{param}` 로 바꾼다.
- 최종 XML 안에 `#year#`, `#month#`, `#searchKeyword#`, `#restdeNo#` 같은 iBATIS placeholder가 남아 있으면 안 된다.

### 4. typeAlias 처리
- 원본 XML 안의 typeAlias 선언은 다음과 같다.
- `egovMap` → `egovframework.rte.psl.dataaccess.util.EgovMap`
- `RestdeVO` → `egovframework.com.sym.cal.service.RestdeVO`
- `Restde` → `egovframework.com.sym.cal.service.Restde`
- 이 근거만 사용해서 alias를 FQCN으로 치환하라.
- 최종 XML 안에 `<typeAlias>` 태그를 남기지 마라.
- 이 파일에서는 alias를 FQCN으로 확정할 수 있으므로 “alias를 FQCN으로 확정할 수 없음” TODO를 반복해서 넣지 마라.

### 5. 동적 SQL 변환
- 원본의 다음 구문은 `prepend="AND"` 를 갖고 있다.
- `<isEqual prepend="AND" property="searchCondition" compareValue="1">`
- `<isEqual prepend="AND" property="searchCondition" compareValue="2">`
- 이 구문은 MyBatis `<if>` 로 바꾸되, 반드시 SQL 안에 `AND` 를 포함해야 한다.

올바른 예:
`<if test="searchCondition == '1'">`
`<![CDATA[AND A.RESTDE = #{searchKeyword}]]>`
`</if>`

잘못된 예:
`<if test="searchCondition == '1'">`
`<![CDATA[A.RESTDE = #{searchKeyword}]]>`
`</if>`

- `selectRestdeListTotCnt` 쿼리도 같은 규칙을 적용한다.

### 6. `<if test>` XML 문법
- `<if test="...">` 의 따옴표는 반드시 정상적으로 닫혀야 한다.
- XML 속성 문법이 깨지면 안 된다.
- 올바름: `<if test="searchCondition == '1'">`
- 잘못됨: `<if test="searchCondition == '1'>`

### 7. `$param$` TODO 금지 조건
- 원본 SQL 본문에 실제 `$param$` 패턴이 없으면 `$param$` 관련 TODO를 넣지 마라.
- 원본 주석에 `$->#변경` 이력이 있어도 현재 SQL 본문에 `$param$` 가 없으면 TODO를 넣지 않는다.

### 8. SQL 변경 금지
- SQL 문장 자체는 바꾸지 않는다.
- 테이블명, 컬럼명, 함수명, 조건식 의미를 바꾸지 않는다.
- Oracle SQL 방언도 그대로 유지한다.
- 단, iBATIS placeholder 문법만 MyBatis placeholder 문법으로 바꾼다.
- dynamic tag는 MyBatis 형식으로 바꾸되 SQL 의미는 그대로 유지한다.

## 이 파일에서 기대하는 대표 변환 포인트
- `<sqlMap namespace="RestdeManage">` → `<mapper namespace="RestdeManage">`
- `parameterClass="Restde"` → `parameterType="egovframework.com.sym.cal.service.Restde"`
- `parameterClass="RestdeVO"` → `parameterType="egovframework.com.sym.cal.service.RestdeVO"`
- `resultClass="egovMap"` → `resultType="egovframework.rte.psl.dataaccess.util.EgovMap"`
- `resultClass="Restde"` → `resultType="egovframework.com.sym.cal.service.Restde"`
- `<typeAlias>` 태그 제거
- `#searchKeyword#` → `#{searchKeyword}`
- `#firstIndex#` → `#{firstIndex}`
- `#recordCountPerPage#` → `#{recordCountPerPage}`
- `prepend="AND"` 조건은 `<if>` 내부 SQL에 `AND` 포함

## 출력 전 자체 검증
- JSON 형식이 아닌가
- `create_new_file` 같은 wrapper가 없는가
- XML declaration이 있는가
- `<mapper namespace="RestdeManage">` 인가
- `<typeAlias>` 가 남아 있지 않은가
- `parameterClass=` 가 남아 있지 않은가
- `resultClass=` 가 남아 있지 않은가
- `#...#` placeholder가 남아 있지 않은가
- `<isEqual` 가 남아 있지 않은가
- `<if test="...">` 문법이 정상인가
- `selectRestdeList`, `selectRestdeListTotCnt` 의 동적 조건에 `AND` 가 들어가 있는가
- 실제 `$param$` 가 없는데 `$param$` TODO를 넣지 않았는가
- `수동검토 필요 항목` 섹션에 실제로 발견되지 않은 항목을 관성적으로 적지 않았는가
- 실제 수동검토 필요 항목이 없으면 `없음` 으로 작성했는가

위 조건 중 하나라도 만족하지 못하면 다시 수정한 후 출력하라.

## 답변 언어
- 설명은 한국어로 작성한다.
- XML tag, attribute, class명, package명, namespace, statement id, 파일 경로는 원문 그대로 유지한다.
