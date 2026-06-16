너는 선택된 DAO Java 파일을 eGovFrame 4.3 MyBatis 기준으로 직접 변환한다.

반드시 실제 소스를 변경하라.
"No changes are necessary", "Already compliant", "No conversion required" 라고 답하지 마라.

## 필수 변환

아래 패턴이 있으면 무조건 변환한다.

extends EgovComAbstractDAO
→ extends EgovAbstractMapper

extends EgovAbstractDAO
→ extends EgovAbstractMapper

list(
→ selectList(

select(
→ selectOne(

단, insert(), update(), delete()는 유지한다.

## import 규칙

아래 import를 추가한다.

import egovframework.rte.psl.dataaccess.EgovAbstractMapper;

아래 import는 제거한다.

import egovframework.com.cmm.service.impl.EgovComAbstractDAO;
import egovframework.rte.psl.dataaccess.EgovAbstractDAO;
import com.ibatis.*;

## 유지 규칙

절대 변경하지 마라.

- package
- class name
- @Repository
- method name
- method parameter
- return type
- SQL statement id 문자열
- 주석
- 업무 로직

## 변환 예시

변경 전:

public class CmmUseDAO extends EgovComAbstractDAO {

    @SuppressWarnings("unchecked")
    public List<CmmnDetailCode> selectCmmCodeDetail(ComDefaultCodeVO vo) throws Exception {
        return (List<CmmnDetailCode>) list("CmmUseDAO.selectCmmCodeDetail", vo);
    }
}

변경 후:

public class CmmUseDAO extends EgovAbstractMapper {

    public List<CmmnDetailCode> selectCmmCodeDetail(ComDefaultCodeVO vo) throws Exception {
        return selectList("CmmUseDAO.selectCmmCodeDetail", vo);
    }
}

## 저장 규칙

원본 파일은 수정하지 않는다.
변환 파일은 source 경로를 converted 경로로 바꾼 동일 위치에 생성한다.

예:

source/프로젝트/src/main/java/...
→
converted/프로젝트/src/main/java/...

## 출력 규칙

채팅에는 아래만 출력한다.

변경 요약:
- 실제 변경한 내용

생성 대상 경로:
- converted 하위 경로