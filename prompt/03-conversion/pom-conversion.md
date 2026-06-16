eGovFrame 3.1 pom.xml을 eGovFrame 4.3 기준 pom.xml 후보로 변환하라.

## 목표
- 기존 pom.xml의 dependency 의도를 최대한 유지한다.
- eGovFrame 4.3 기준으로 변환한다.
- 확인된 Maven 좌표만 사용한다.
- 확인되지 않은 좌표는 추측하지 않는다.
- 변환 결과는 바로 저장 가능한 `pom.xml` 전체 형태로 출력한다.

## 절대 규칙
- 존재하지 않는 groupId, artifactId, version을 추측해서 만들지 마라.
- groupId만 바꾸거나 artifactId만 바꾸는 부분 변환을 하지 마라.
- 변경전 좌표와 변경후 좌표를 혼용하지 마라.
- 표에 없는 eGov dependency는 추측 변환하지 마라.
- 확인되지 않은 항목은 `TODO` XML 주석으로 남겨라.
- eGov dependency는 반드시 아래 규칙과 표를 최우선 기준으로 적용하라.

## eGov dependency 확정 좌표 변환표
아래 표에 있는 항목은 반드시 표 기준으로 변환한다.

| 변경전 groupId | 변경전 artifactId | 변경후 groupId | 변경후 artifactId |
|---|---|---|---|
| `egovframework.rte` | `egovframework.rte.ptl.mvc` | `org.egovframe.rte` | `org.egovframe.rte.ptl.mvc` |
| `egovframework.rte` | `egovframework.rte.psl.dataaccess` | `org.egovframe.rte` | `org.egovframe.rte.psl.dataaccess` |
| `egovframework.rte` | `egovframework.rte.fdl.idgnr` | `org.egovframe.rte` | `org.egovframe.rte.fdl.idgnr` |
| `egovframework.rte` | `egovframework.rte.fdl.property` | `org.egovframe.rte` | `org.egovframe.rte.fdl.property` |
| `egovframework.rte` | `egovframework.rte.fdl.security` | `org.egovframe.rte` | `org.egovframe.rte.fdl.security` |
| `egovframework.rte` | `egovframework.rte.fdl.excel` | `org.egovframe.rte` | `org.egovframe.rte.fdl.excel` |
| `egovframework.rte` | `egovframework.rte.fdl.cmmn` | `org.egovframe.rte` | `org.egovframe.rte.fdl.cmmn` |
| `egovframework.rte` | `egovframework.rte.fdl.crypto` | `org.egovframe.rte` | `org.egovframe.rte.fdl.crypto` |
| `egovframework.rte` | `egovframework.rte.fdl.logging` | `org.egovframe.rte` | `org.egovframe.rte.fdl.logging` |
| `egovframework.rte` | `egovframework.rte.fdl.string` | `org.egovframe.rte` | `org.egovframe.rte.fdl.string` |

## eGov dependency 검증 필요 좌표
아래 항목은 이름이 비슷하다고 해서 자동 변환하지 마라.

- `egovframework.com:*`
- `egovframework.com.cmm:*`
- `egovframework.com.utl.fcc:*`
- `egovframework.com.utl.sim:*`
- `egovframework.com.ems:*`
- 그 외 모든 `egovframework.com...` 계열

이 계열은 다음 조건을 모두 만족할 때만 변환한다.
- eGovFrame 4.3 공식 샘플 POM 또는
- eGovFrame 공식 Maven 저장소에서
- 정확히 동일한 변경후 좌표가 확인된 경우

확인되지 않으면:
- 추측 변환 금지
- 해당 dependency 위에 `TODO` XML 주석 추가
- 왜 확인이 필요한지 한 줄로 남겨라

예시 주석:
`<!-- TODO: eGovFrame 4.3 공식 좌표 확인 필요. 추측 변환 금지 -->`

## eGov dependency 변환 규칙
- `egovframework.rte.*` 와 `org.egovframe.rte.*` 를 동시에 사용하지 않는다.
- `egovframework.com.*` 와 `org.egovframe.com.*` 를 동시에 사용하지 않는다.
- 표에 있는 `rte` 계열은 반드시 표 기준으로 치환한다.
- 표에 없는 eGov dependency는 공식 근거가 없는 한 변환하지 않는다.
- `egovframework.com.ems:sndng-mail` 같은 항목은 이름 유사성만으로 다른 좌표로 바꾸지 마라.

## 버전 및 property 규칙
- eGovFrame 4.3 RTE 버전 property는 다음 형식을 우선 사용한다.

`<org.egovframe.rte.version>4.3.0</org.egovframe.rte.version>`

- 기존의 `<egovframework.rte.version>` 를 그대로 유지하지 말고, `org.egovframe.rte` 좌표를 쓰는 경우에는 property 명도 함께 정리하라.
- version이 확실하지 않은 dependency는 임의 버전 지정 금지, `TODO` 주석으로 남겨라.

## eGov RTE version property 절대 규칙

eGovFrame 4.3 RTE dependency를 사용하는 경우 version property는 반드시 아래 이름만 사용한다.

```xml
<org.egovframe.rte.version>4.3.0</org.egovframe.rte.version>
```

## repository 규칙
- eGov dependency 확인 및 사용 시 eGovFrame 공식 Maven 저장소를 우선 고려하라.
- Maven Central만 보고 eGov 좌표 존재를 단정하지 마라.
- 공식 저장소 또는 공식 샘플 POM으로 확인되지 않은 eGov 좌표는 생성하지 마라.

## 변환 후 자체 검증 규칙

최종 `pom.xml` 출력 전에 반드시 다음 항목을 자체 검증하라.

- `${egovframework.rte.version}` 문자열이 남아 있으면 실패다.
- `<groupId>egovframework.rte</groupId>`가 남아 있으면 실패다.
- `<artifactId>egovframework.rte.`로 시작하는 artifactId가 남아 있으면 실패다.
- `org.egovframe.rte` groupId와 `egovframework.rte.*` artifactId가 혼용되면 실패다.
- eGov RTE dependency의 version은 모두 `${org.egovframe.rte.version}`를 사용해야 한다.

위 조건을 만족하지 못하면 `pom.xml`을 출력하지 말고 오류 원인을 먼저 설명하라.

## 출력 규칙
다음 순서로 출력하라.

1. 변환된 `pom.xml` 전체
2. 확정 변환된 eGov dependency 목록
3. 좌표 확인이 필요하여 `TODO`로 남긴 항목 목록
4. 수동 검토 필요 항목

## 답변 언어
- 모든 설명은 한국어로 작성한다.
- 단, XML tag, groupId, artifactId, version, 파일명은 원문 그대로 유지한다.
