전자정부프레임워크 3.1 → 4.3 전환 PoC 작업 중이다.

현재 Continue에서 선택된 SQL Map XML 파일을 대상으로 작업한다.

원본 파일은 수정하지 않는다.

반드시 원본 파일의 상대경로를 유지하여 `converted/` 하위에 새로운 파일을 생성한다.

예시)

source/.../AAA.xml

↓

converted/.../AAA.xml

## 작업 목적

선택된 SQL Map XML(iBATIS)을 MyBatis Mapper XML 형식으로 변환한다.

SQL 의미를 변경하지 않는다.

변환 결과는 즉시 저장 가능한 완전한 XML 형태로 출력한다.

## 가장 중요한 출력 규칙

### 금지 사항

다음 형식은 절대 사용하지 마라.

* JSON 객체
* JSON 배열
* create_new_file
* tool call
* function call
* read_file
* open_file
* load_file
* fetch_file
* 파일 읽기 요청
* 준비 단계 설명
* 추가 입력 요청

최종 산출물만 출력한다.

---

## 반드시 지킬 출력 형식

반드시 아래 순서로 출력한다.

### 1. 생성 대상 경로

예시

생성 대상 경로:

`converted/.../파일명.xml`

---

### 2. 변환 결과 XML

반드시 XML Declaration부터 출력한다.

예시

```xml
<?xml version="1.0" encoding="UTF-8"?>
<mapper namespace="...">
...
</mapper>
```

XML 전체 내용을 출력한다.

일부 생략 금지.

---

### 3. 수동검토 필요 항목

반드시 출력한다.

예시

수동검토 필요 항목:

* 실제 발견 항목

또는

수동검토 필요 항목:

* 없음

---

## 수동검토 필요 항목 작성 규칙

실제로 발견된 항목만 작성한다.

관성적으로 체크리스트를 나열하지 마라.

다음과 같은 항목은 실제 발견된 경우에만 작성한다.

* selectKey 사용
* Procedure 호출
* 동적 컬럼 생성
* 동적 테이블명 사용
* 실제 $param$ 사용
* Alias 확정 불가
* 수동 판단이 필요한 Oracle 특수 SQL

실제로 발견되지 않았다면 작성하지 마라.

실제 발견 항목이 없으면 반드시

* 없음

으로 출력한다.

---

# 변환 규칙

## 1. XML 문서 형식

반드시 XML Declaration으로 시작한다.

예시

```xml
<?xml version="1.0" encoding="UTF-8"?>
```

다음은 제거한다.

```xml
<!DOCTYPE sqlMap ...>
```

최종 XML에는 `<sqlMap>` 이 남아 있으면 안 된다.

루트는 반드시 다음 형식으로 변환한다.

```xml
<mapper namespace="원본 namespace">
```

원본 namespace 값은 변경하지 않는다.

---

## 2. namespace 유지

원본 namespace를 그대로 유지한다.

대소문자를 변경하지 않는다.

---

## 3. statement id 유지

모든 statement id는 원본 그대로 유지한다.

대소문자도 변경하지 않는다.

---

## 4. parameterClass 변환

```xml
parameterClass="..."
```

↓

```xml
parameterType="..."
```

---

## 5. resultClass 변환

```xml
resultClass="..."
```

↓

```xml
resultType="..."
```

---

## 6. typeAlias 처리

원본 XML 내부의 `<typeAlias>` 선언을 분석한다.

예시

```xml
<typeAlias
    alias="UserVO"
    type="egovframework.xxx.UserVO"/>
```

↓

```xml
parameterType="egovframework.xxx.UserVO"
```

또는

```xml
resultType="egovframework.xxx.UserVO"
```

확정 가능한 경우 반드시 FQCN으로 치환한다.

최종 XML에 `<typeAlias>` 태그를 남기지 않는다.

원본 XML 내부 정보만으로 확정 불가능한 경우에만 수동검토 항목에 기록한다.

---

## 7. Placeholder 변환

모든 iBATIS Placeholder를 MyBatis 형식으로 변환한다.

예시

```xml
#param#
```

↓

```xml
#{param}
```

최종 XML에

```xml
#param#
```

형식이 남아 있으면 안 된다.

---

## 8. Dynamic SQL 변환

다음 태그들은 MyBatis 형식으로 변환한다.

예시

```xml
<isEqual>
```

↓

```xml
<if>
```

```xml
<isNotEqual>
```

↓

```xml
<if>
```

```xml
<isNotNull>
```

↓

```xml
<if>
```

```xml
<isNotEmpty>
```

↓

```xml
<if>
```

---

## 9. prepend 의미 보존

다음과 같은 패턴이 존재하는 경우

```xml
<isEqual prepend="AND" ...>
```

변환 후 반드시 SQL 내부에 AND를 유지한다.

올바른 예

```xml
<if test="...">
    <![CDATA[
    AND COLUMN = #{value}
    ]]>
</if>
```

잘못된 예

```xml
<if test="...">
    <![CDATA[
    COLUMN = #{value}
    ]]>
</if>
```

prepend="OR" 도 동일하게 의미를 보존한다.

---

## 10. XML 문법 보장

모든

```xml
<if test="...">
```

는 정상 XML 문법이어야 한다.

예시

올바름

```xml
<if test="searchCondition == '1'">
```

잘못됨

```xml
<if test="searchCondition == '1'>
```

---

## 11. $param$ 처리 규칙

원본 SQL 본문에 실제

```xml
$param$
```

패턴이 존재하는 경우에만 수동검토 항목에 기록한다.

주석에 과거 변경 이력이 있다고 해서 사용 중이라고 판단하지 마라.

실제 SQL 본문에 존재하지 않으면 언급하지 마라.

---

## 12. SQL 변경 금지

다음 항목은 변경하지 않는다.

* SQL 의미
* 테이블명
* 컬럼명
* 함수명
* 조건식
* Oracle 방언

허용되는 변경은 다음뿐이다.

* iBATIS → MyBatis 문법 변환
* typeAlias 제거
* parameterClass → parameterType
* resultClass → resultType
* Dynamic SQL 태그 변환

---

## 13. 생성 파일 정책

원본 파일은 수정하지 않는다.

반드시 converted 하위 동일 상대경로에 생성한다고 가정한다.

---

# 출력 전 자체 검증

다음 항목을 모두 확인한 후 출력한다.

* JSON 형식이 아닌가
* create_new_file wrapper가 없는가
* tool call 형식이 없는가
* XML Declaration이 존재하는가
* 루트가 mapper인가
* namespace가 유지되었는가
* typeAlias가 제거되었는가
* parameterClass가 남아있지 않은가
* resultClass가 남아있지 않은가
* #...# placeholder가 남아있지 않은가
* isEqual/isNotEqual/isNotNull/isNotEmpty가 남아있지 않은가
* prepend 의미가 보존되었는가
* if test 문법이 정상인가
* 실제 $param$ 가 없는데 수동검토에 작성하지 않았는가
* 수동검토 항목이 실제 발견 사항만 포함하는가
* 발견 사항이 없으면 "없음"으로 출력했는가

위 조건 중 하나라도 만족하지 못하면 수정 후 다시 출력한다.

## 답변 언어

설명은 한국어로 작성한다.

XML tag, attribute, class명, package명, namespace, statement id, SQL 구문은 원문을 유지한다.
