import argparse
import json
from pathlib import Path
from urllib.request import Request, urlopen

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "qwen3-coder:30b"


def read_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"파일이 없습니다: {path}")
    return file_path.read_text(encoding="utf-8")


def build_prompt(policy: str, analysis_prompt: str, targets: list[str]) -> str:
    from pathlib import Path

    target_sections = []

    for path in targets:
        content = read_file(path)

        print(f"[LOAD] {path}")
        print(f"[SIZE] {len(content)} chars")

        suffix = Path(path).suffix.lower()
        name = Path(path).name

        if suffix == ".java":
            file_type = "JAVA_DAO"
        elif suffix == ".xml":
            file_type = "SQLMAP_XML"
        else:
            file_type = "UNKNOWN"

        target_sections.append(
            f"""
==============================
[분석 대상 파일]
==============================
FILE_TYPE: {file_type}
FILE_NAME: {name}
FILE_PATH: {path}
CONTENT_LENGTH: {len(content)} chars

{content}
"""
        )

    return f"""
너는 전자정부프레임워크 3.x → 4.3 전환 분석 전문가다.

아래 전환 정책과 분석 프롬프트를 반드시 준수하라.
추측하지 말고, 확인 불가능한 내용은 "확인 필요"로 표시하라.
소스 수정은 절대 하지 말고 분석 결과만 출력하라.

==============================
[전환 정책]
==============================

{policy}

==============================
[분석 프롬프트]
==============================

{analysis_prompt}

==============================
[분석 대상]
==============================

{"".join(target_sections)}
"""


def call_ollama(model: str, prompt: str) -> str:
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0,
            "top_p": 0.8,
            "num_ctx": 8192
        }
    }

    req = Request(
        OLLAMA_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urlopen(req, timeout=600) as response:
            result = json.loads(response.read().decode("utf-8"))
            return result.get("response", "")
    except Exception as e:
        if hasattr(e, "read"):
            error_body = e.read().decode("utf-8", errors="replace")
            print("Ollama error body:")
            print(error_body)
        raise  


def save_result(output_path: str, content: str) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(
        description="Qwen3-Coder Ollama 기반 eGovFrame 분석 실행"
    )

    parser.add_argument(
        "--policy",
        required=True,
        help="migration-policy.md 경로"
    )

    parser.add_argument(
        "--prompt",
        required=True,
        help="분석 프롬프트 md 경로"
    )

    parser.add_argument(
        "--target",
        required=True,
        nargs="+",
        help="분석 대상 파일 목록"
    )

    parser.add_argument(
        "--output",
        required=True,
        help="결과 저장 파일"
    )

    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Ollama 모델명 (기본값: {DEFAULT_MODEL})"
    )

    args = parser.parse_args()

    print("파일 로딩 중...")

    print("[DEBUG] targets:")
    for target in args.target:
        print(f" - {target}")
    
    policy = read_file(args.policy)
    analysis_prompt = read_file(args.prompt)

    full_prompt = build_prompt(
        policy=policy,
        analysis_prompt=analysis_prompt,
        targets=args.target
    )

    print("분석 요청 중...")
    print(f"모델: {args.model}")
    print(f"대상 파일 수: {len(args.target)}")

    result = call_ollama(
        model=args.model,
        prompt=full_prompt
    )

    save_result(args.output, result)

    print("분석 완료")
    print(f"결과 저장: {args.output}")


if __name__ == "__main__":
    main()