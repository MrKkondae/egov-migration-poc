#!/usr/bin/env python3
"""Extract Maven pom.xml metadata into CSV files for migration analysis.

Usage examples:
    python scripts/extract_pom_dependencies.py --root source/cf-egovboard-war
    python scripts/extract_pom_dependencies.py --pom pom.xml

Result examples:
    dependency.csv:
        sourcePom,groupId,artifactId,version,scope,optional
        source/app/pom.xml,org.springframework,spring-core,5.3.39,compile,false

    summary.md:
        ## Summary
        - pom.xml 개수: 3
        - dependency 개수: 42

Generated files:
    output/pom-analysis/dependency.csv
    output/pom-analysis/dependency-management.csv
    output/pom-analysis/exclusions.csv
    output/pom-analysis/properties.csv
    output/pom-analysis/parent.csv
    output/pom-analysis/packaging.csv
    output/pom-analysis/summary.md
    output/pom-analysis/dependency-category.csv
    output/pom-analysis/dependency-category-summary.md
    output/pom-analysis/categories/*.csv
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, Sequence
import xml.etree.ElementTree as ET


OUTPUT_DIR = Path("output/pom-analysis")
CATEGORY_OUTPUT_DIR = OUTPUT_DIR / "categories"
EXCLUDED_DIR_NAMES = {".git", ".venv", "node_modules", "target"}
CATEGORY_ORDER = [
    "egov",
    "spring",
    "ibatis",
    "mybatis",
    "servlet",
    "jsp",
    "jstl",
    "logging",
    "cache",
    "datasource",
    "database",
    "test",
    "security",
    "mail",
    "file",
    "xml",
    "scheduler",
    "web-ui",
    "vendor",
    "system",
    "legacy",
    "unknown",
]
PRIMARY_CATEGORY_ORDER = [
    "egov",
    "ibatis",
    "mybatis",
    "servlet",
    "jsp",
    "jstl",
    "logging",
    "cache",
    "datasource",
    "database",
    "security",
    "mail",
    "file",
    "xml",
    "scheduler",
    "web-ui",
    "vendor",
    "system",
    "legacy",
    "spring",
    "test",
    "unknown",
]
HIGH_PRIORITY_CATEGORIES = {
    "egov",
    "ibatis",
    "mybatis",
    "servlet",
    "jsp",
    "jstl",
    "cache",
    "datasource",
    "vendor",
    "system",
    "legacy",
}
MEDIUM_PRIORITY_CATEGORIES = {
    "logging",
    "database",
    "security",
    "mail",
    "file",
    "xml",
    "scheduler",
    "web-ui",
}
LOW_PRIORITY_CATEGORIES = {"spring", "test", "unknown"}
CATEGORY_RULES = {
    "egov": ["egovframework", "org.egovframe", "egovframework.com"],
    "spring": ["org.springframework", "spring-"],
    "ibatis": ["ibatis", "sqlmap"],
    "mybatis": ["mybatis"],
    "servlet": ["servlet", "javax.servlet", "jakarta.servlet"],
    "jsp": ["jsp", "javax.servlet.jsp"],
    "jstl": ["jstl", "taglibs", "standard"],
    "logging": ["log4j", "slf4j", "logback", "commons-logging", "log4jdbc"],
    "cache": ["ehcache", "terracotta", "cache-api"],
    "datasource": ["dbcp", "hikari", "tomcat-jdbc", "datasource"],
    "database": ["mysql", "oracle", "postgresql", "mariadb", "hsqldb", "h2", "jdbc"],
    "test": ["junit", "mockito", "hamcrest", "assertj", "dbunit", "spring-test"],
    "security": ["security", "jasypt", "crypto", "encryption", "bcrypt", "sso"],
    "mail": ["mail", "email", "ems", "sndng-mail"],
    "file": ["fileupload", "commons-io", "compress", "poi", "excel", "jodconverter"],
    "xml": ["xerces", "xml", "xbean", "xmlbeans", "batik", "antlr"],
    "scheduler": ["quartz", "scheduler"],
    "web-ui": ["ajaxtags", "ckeditor", "tiles", "sitemesh", "struts", "twitter4j"],
    "vendor": [
        "weblogic",
        "jeus",
        "websphere",
        "tmax",
        "oz",
        "clipreport",
        "rexpert",
        "xplatform",
        "oracle",
    ],
    "legacy": [
        "ibatis",
        "oro",
        "ajaxtags",
        "ehcache-core",
        "ehcache-terracotta",
        "servlet-api",
        "jsp-api",
        "standard",
    ],
}


@dataclass(frozen=True)
class DependencyRecord:
    source_pom: str
    group_id: str
    artifact_id: str
    version: str
    scope: str
    optional: str
    system_path: str


@dataclass(frozen=True)
class DependencyManagementRecord:
    source_pom: str
    group_id: str
    artifact_id: str
    version: str
    scope: str
    type_value: str
    import_scope: str


@dataclass(frozen=True)
class ExclusionRecord:
    source_pom: str
    parent_group_id: str
    parent_artifact_id: str
    exclusion_group_id: str
    exclusion_artifact_id: str


@dataclass(frozen=True)
class PropertyRecord:
    source_pom: str
    property_name: str
    property_value: str


@dataclass(frozen=True)
class ParentRecord:
    source_pom: str
    group_id: str
    artifact_id: str
    version: str


@dataclass(frozen=True)
class PackagingRecord:
    source_pom: str
    packaging: str


@dataclass(frozen=True)
class MatchReason:
    category: str
    text: str


@dataclass(frozen=True)
class ClassifiedDependencyRecord:
    source_pom: str
    group_id: str
    artifact_id: str
    version: str
    scope: str
    optional: str
    categories: list[str]
    primary_category: str
    priority: str
    reason: str


@dataclass
class AnalysisResult:
    pom_count: int
    dependencies: list[DependencyRecord]
    dependency_management: list[DependencyManagementRecord]
    exclusions: list[ExclusionRecord]
    properties: list[PropertyRecord]
    parents: list[ParentRecord]
    packaging: list[PackagingRecord]
    classified_dependencies: list[ClassifiedDependencyRecord]
    errors: list[str]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract dependency metadata from one or more Maven pom.xml files."
    )
    parser.add_argument(
        "--root",
        type=Path,
        help="Root directory to recursively scan for pom.xml files.",
    )
    parser.add_argument(
        "--pom",
        action="append",
        type=Path,
        default=[],
        help="Path to a pom.xml file. Can be provided multiple times.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pom_paths = collect_pom_paths(args.root, args.pom)
    if not pom_paths:
        print("No pom.xml files found.")
        return 1

    result = analyze_poms(pom_paths)
    write_outputs(result)

    if result.errors:
        print("Completed with errors:")
        for error in result.errors:
            print(f"- {error}")
        return 2

    print(f"Processed {result.pom_count} pom.xml file(s).")
    print(f"Output written to {OUTPUT_DIR}")
    return 0


def collect_pom_paths(root: Path | None, pom_args: Sequence[Path]) -> list[Path]:
    pom_paths: set[Path] = set()

    if root is not None:
        if not root.exists():
            raise FileNotFoundError(f"Root path does not exist: {root}")
        for pom_path in discover_poms(root):
            pom_paths.add(pom_path.resolve())

    for pom_arg in pom_args:
        if not pom_arg.exists():
            raise FileNotFoundError(f"POM path does not exist: {pom_arg}")
        if pom_arg.is_dir():
            raise IsADirectoryError(f"Expected a pom.xml file, got directory: {pom_arg}")
        pom_paths.add(pom_arg.resolve())

    return sorted(pom_paths)


def discover_poms(root: Path) -> Iterator[Path]:
    stack = [root]
    while stack:
        current = stack.pop()
        try:
            entries = sorted(current.iterdir(), key=lambda entry: entry.name)
        except OSError:
            continue

        for entry in reversed(entries):
            if entry.is_dir():
                if entry.name not in EXCLUDED_DIR_NAMES:
                    stack.append(entry)
                continue
            if entry.is_file() and entry.name == "pom.xml":
                yield entry


def analyze_poms(pom_paths: Sequence[Path]) -> AnalysisResult:
    dependencies: list[DependencyRecord] = []
    dependency_management: list[DependencyManagementRecord] = []
    exclusions: list[ExclusionRecord] = []
    properties: list[PropertyRecord] = []
    parents: list[ParentRecord] = []
    packaging: list[PackagingRecord] = []
    errors: list[str] = []

    for pom_path in pom_paths:
        try:
            tree = ET.parse(pom_path)
            root = tree.getroot()
            source_pom = normalize_source_path(pom_path)

            dependencies.extend(extract_dependencies(root, source_pom))
            dependency_management.extend(extract_dependency_management(root, source_pom))
            exclusions.extend(extract_exclusions(root, source_pom))
            properties.extend(extract_properties(root, source_pom))

            parent = extract_parent(root, source_pom)
            if parent is not None:
                parents.append(parent)

            packaging.append(extract_packaging(root, source_pom))
        except ET.ParseError as exc:
            errors.append(f"{pom_path}: XML parse error: {exc}")
        except OSError as exc:
            errors.append(f"{pom_path}: file read error: {exc}")

    classified_dependencies = [classify_dependency(record) for record in dependencies]
    return AnalysisResult(
        pom_count=len(pom_paths),
        dependencies=dependencies,
        dependency_management=dependency_management,
        exclusions=exclusions,
        properties=properties,
        parents=parents,
        packaging=packaging,
        classified_dependencies=classified_dependencies,
        errors=errors,
    )


def normalize_source_path(path: Path) -> str:
    try:
        return path.relative_to(Path.cwd()).as_posix()
    except ValueError:
        return path.as_posix()


def local_name(tag: str) -> str:
    if tag.startswith("{"):
        return tag.split("}", 1)[1]
    return tag


def child_elements(element: ET.Element, name: str | None = None) -> Iterator[ET.Element]:
    for child in list(element):
        if not isinstance(child.tag, str):
            continue
        if name is None or local_name(child.tag) == name:
            yield child


def find_child(element: ET.Element, name: str) -> ET.Element | None:
    return next(child_elements(element, name), None)


def child_text(element: ET.Element, name: str, default: str = "") -> str:
    child = find_child(element, name)
    if child is None or child.text is None:
        return default
    return child.text.strip()


def extract_dependencies(root: ET.Element, source_pom: str) -> list[DependencyRecord]:
    records: list[DependencyRecord] = []

    def visit(element: ET.Element, in_management: bool, in_exclusions: bool) -> None:
        tag_name = local_name(element.tag)
        next_in_management = in_management or tag_name == "dependencyManagement"
        next_in_exclusions = in_exclusions or tag_name == "exclusions"

        if tag_name == "dependencies" and not next_in_management and not next_in_exclusions:
            for dependency in child_elements(element, "dependency"):
                records.append(build_dependency_record(source_pom, dependency))

        for child in child_elements(element):
            visit(child, next_in_management, next_in_exclusions)

    visit(root, in_management=False, in_exclusions=False)
    return records


def build_dependency_record(source_pom: str, dependency: ET.Element) -> DependencyRecord:
    return DependencyRecord(
        source_pom=source_pom,
        group_id=child_text(dependency, "groupId"),
        artifact_id=child_text(dependency, "artifactId"),
        version=child_text(dependency, "version"),
        scope=child_text(dependency, "scope", default="compile") or "compile",
        optional=normalize_bool_text(child_text(dependency, "optional", default="false")),
        system_path=child_text(dependency, "systemPath"),
    )


def extract_dependency_management(
    root: ET.Element, source_pom: str
) -> list[DependencyManagementRecord]:
    records: list[DependencyManagementRecord] = []

    for management in root.iter():
        if not isinstance(management.tag, str):
            continue
        if local_name(management.tag) != "dependencyManagement":
            continue

        for dependencies in child_elements(management, "dependencies"):
            for dependency in child_elements(dependencies, "dependency"):
                scope = child_text(dependency, "scope")
                type_value = child_text(dependency, "type")
                records.append(
                    DependencyManagementRecord(
                        source_pom=source_pom,
                        group_id=child_text(dependency, "groupId"),
                        artifact_id=child_text(dependency, "artifactId"),
                        version=child_text(dependency, "version"),
                        scope=scope,
                        type_value=type_value,
                        import_scope="true" if scope == "import" else "false",
                    )
                )
    return records


def extract_exclusions(root: ET.Element, source_pom: str) -> list[ExclusionRecord]:
    records: list[ExclusionRecord] = []

    for dependencies in root.iter():
        if not isinstance(dependencies.tag, str):
            continue
        if local_name(dependencies.tag) != "dependencies":
            continue

        for dependency in child_elements(dependencies, "dependency"):
            parent_group_id = child_text(dependency, "groupId")
            parent_artifact_id = child_text(dependency, "artifactId")

            for exclusions in child_elements(dependency, "exclusions"):
                for exclusion in child_elements(exclusions, "exclusion"):
                    records.append(
                        ExclusionRecord(
                            source_pom=source_pom,
                            parent_group_id=parent_group_id,
                            parent_artifact_id=parent_artifact_id,
                            exclusion_group_id=child_text(exclusion, "groupId"),
                            exclusion_artifact_id=child_text(exclusion, "artifactId"),
                        )
                    )
    return records


def extract_properties(root: ET.Element, source_pom: str) -> list[PropertyRecord]:
    properties_element = find_child(root, "properties")
    if properties_element is None:
        return []

    records: list[PropertyRecord] = []
    for property_element in child_elements(properties_element):
        records.append(
            PropertyRecord(
                source_pom=source_pom,
                property_name=local_name(property_element.tag),
                property_value=(property_element.text or "").strip(),
            )
        )
    return records


def extract_parent(root: ET.Element, source_pom: str) -> ParentRecord | None:
    parent = find_child(root, "parent")
    if parent is None:
        return None
    return ParentRecord(
        source_pom=source_pom,
        group_id=child_text(parent, "groupId"),
        artifact_id=child_text(parent, "artifactId"),
        version=child_text(parent, "version"),
    )


def extract_packaging(root: ET.Element, source_pom: str) -> PackagingRecord:
    packaging = child_text(root, "packaging", default="jar") or "jar"
    return PackagingRecord(source_pom=source_pom, packaging=packaging)


def normalize_bool_text(value: str) -> str:
    return "true" if value.strip().lower() == "true" else "false"


def classify_dependency(record: DependencyRecord) -> ClassifiedDependencyRecord:
    matches = find_category_matches(record)
    categories = ordered_categories(matches)
    primary_category = select_primary_category(categories)
    priority = category_to_priority(primary_category)
    reason = build_classification_reason(matches, primary_category)
    return ClassifiedDependencyRecord(
        source_pom=record.source_pom,
        group_id=record.group_id,
        artifact_id=record.artifact_id,
        version=record.version,
        scope=record.scope,
        optional=record.optional,
        categories=categories,
        primary_category=primary_category,
        priority=priority,
        reason=reason,
    )


def find_category_matches(record: DependencyRecord) -> list[MatchReason]:
    matches: list[MatchReason] = []
    group_id = record.group_id.lower()
    artifact_id = record.artifact_id.lower()
    scope = record.scope.lower()

    for category in CATEGORY_ORDER:
        if category == "unknown":
            continue
        if category == "system" and is_system_dependency(record):
            matches.append(MatchReason(category="system", text=system_reason(record)))
            continue
        if category == "test" and scope == "test":
            matches.append(MatchReason(category="test", text="scope is test"))
            continue

        keyword = first_matching_keyword(group_id, artifact_id, CATEGORY_RULES.get(category, ()))
        if keyword is not None:
            matches.append(
                MatchReason(
                    category=category,
                    text=keyword_reason(group_id, artifact_id, keyword),
                )
            )

    if not matches:
        matches.append(MatchReason(category="unknown", text="no category rules matched"))
    return deduplicate_matches(matches)


def is_system_dependency(record: DependencyRecord) -> bool:
    return record.scope.lower() == "system" or bool(record.system_path.strip())


def system_reason(record: DependencyRecord) -> str:
    if record.scope.lower() == "system":
        return "scope is system"
    return "systemPath is present"


def first_matching_keyword(
    group_id: str, artifact_id: str, keywords: Iterable[str]
) -> str | None:
    for keyword in keywords:
        lowered_keyword = keyword.lower()
        if lowered_keyword in group_id or lowered_keyword in artifact_id:
            return keyword
    return None


def keyword_reason(group_id: str, artifact_id: str, keyword: str) -> str:
    lowered_keyword = keyword.lower()
    if lowered_keyword in artifact_id:
        return f"artifactId contains {keyword}"
    if lowered_keyword in group_id:
        return f"groupId contains {keyword}"
    return f"groupId or artifactId contains {keyword}"


def deduplicate_matches(matches: list[MatchReason]) -> list[MatchReason]:
    seen_categories: set[str] = set()
    deduplicated: list[MatchReason] = []
    for match in matches:
        if match.category in seen_categories:
            continue
        seen_categories.add(match.category)
        deduplicated.append(match)
    return deduplicated


def ordered_categories(matches: list[MatchReason]) -> list[str]:
    matched_categories = {match.category for match in matches}
    return [category for category in CATEGORY_ORDER if category in matched_categories]


def select_primary_category(categories: list[str]) -> str:
    for category in PRIMARY_CATEGORY_ORDER:
        if category in categories:
            return category
    return "unknown"


def category_to_priority(primary_category: str) -> str:
    if primary_category in HIGH_PRIORITY_CATEGORIES:
        return "high"
    if primary_category in MEDIUM_PRIORITY_CATEGORIES:
        return "medium"
    if primary_category in LOW_PRIORITY_CATEGORIES:
        return "low"
    return "low"


def build_classification_reason(
    matches: Sequence[MatchReason], primary_category: str
) -> str:
    for match in matches:
        if match.category == primary_category:
            return match.text
    return matches[0].text


def write_outputs(result: AnalysisResult) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    CATEGORY_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    write_csv(
        OUTPUT_DIR / "dependency.csv",
        ["sourcePom", "groupId", "artifactId", "version", "scope", "optional"],
        (
            [
                record.source_pom,
                record.group_id,
                record.artifact_id,
                record.version,
                record.scope,
                record.optional,
            ]
            for record in result.dependencies
        ),
    )
    write_csv(
        OUTPUT_DIR / "dependency-management.csv",
        ["sourcePom", "groupId", "artifactId", "version", "scope", "type", "importScope"],
        (
            [
                record.source_pom,
                record.group_id,
                record.artifact_id,
                record.version,
                record.scope,
                record.type_value,
                record.import_scope,
            ]
            for record in result.dependency_management
        ),
    )
    write_csv(
        OUTPUT_DIR / "exclusions.csv",
        [
            "sourcePom",
            "parentGroupId",
            "parentArtifactId",
            "exclusionGroupId",
            "exclusionArtifactId",
        ],
        (
            [
                record.source_pom,
                record.parent_group_id,
                record.parent_artifact_id,
                record.exclusion_group_id,
                record.exclusion_artifact_id,
            ]
            for record in result.exclusions
        ),
    )
    write_csv(
        OUTPUT_DIR / "properties.csv",
        ["sourcePom", "propertyName", "propertyValue"],
        (
            [record.source_pom, record.property_name, record.property_value]
            for record in result.properties
        ),
    )
    write_csv(
        OUTPUT_DIR / "parent.csv",
        ["sourcePom", "groupId", "artifactId", "version"],
        (
            [record.source_pom, record.group_id, record.artifact_id, record.version]
            for record in result.parents
        ),
    )
    write_csv(
        OUTPUT_DIR / "packaging.csv",
        ["sourcePom", "packaging"],
        ([record.source_pom, record.packaging] for record in result.packaging),
    )
    write_dependency_category_outputs(result.classified_dependencies)
    write_summary(OUTPUT_DIR / "summary.md", result)


def write_csv(path: Path, headers: Sequence[str], rows: Iterable[Sequence[str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(rows)


def write_dependency_category_outputs(
    rows: Sequence[ClassifiedDependencyRecord],
) -> None:
    headers = [
        "sourcePom",
        "groupId",
        "artifactId",
        "version",
        "scope",
        "optional",
        "categories",
        "primaryCategory",
        "priority",
        "reason",
    ]
    write_csv(
        OUTPUT_DIR / "dependency-category.csv",
        headers,
        (classified_dependency_to_row(record) for record in rows),
    )
    write_dependency_category_summary(
        OUTPUT_DIR / "dependency-category-summary.md",
        rows,
    )
    write_category_csv_files(rows, headers)


def classified_dependency_to_row(record: ClassifiedDependencyRecord) -> list[str]:
    return [
        record.source_pom,
        record.group_id,
        record.artifact_id,
        record.version,
        record.scope,
        record.optional,
        ";".join(record.categories),
        record.primary_category,
        record.priority,
        record.reason,
    ]


def write_category_csv_files(
    rows: Sequence[ClassifiedDependencyRecord], headers: Sequence[str]
) -> None:
    for category in CATEGORY_ORDER:
        write_csv(
            CATEGORY_OUTPUT_DIR / f"{category}.csv",
            headers,
            (
                classified_dependency_to_row(record)
                for record in rows
                if category in record.categories
            ),
        )


def write_dependency_category_summary(
    path: Path, rows: Sequence[ClassifiedDependencyRecord]
) -> None:
    category_counts = count_categories(rows)
    priority_counts = count_priorities(rows)
    unknown_rows = [record for record in rows if "unknown" in record.categories]
    high_priority_rows = [record for record in rows if record.priority == "high"]
    matched_count = sum(1 for record in rows if "unknown" not in record.categories)

    lines = [
        "## Summary",
        "",
        f"* 전체 dependency 수: {len(rows)}",
        f"* 카테고리 매칭 dependency 수: {matched_count}",
        f"* unknown dependency 수: {len(unknown_rows)}",
        f"* high priority 수: {priority_counts['high']}",
        f"* medium priority 수: {priority_counts['medium']}",
        f"* low priority 수: {priority_counts['low']}",
        "",
        "## Category Counts",
        "",
        "| category | count |",
        "| --- | --- |",
    ]

    for category in CATEGORY_ORDER:
        lines.append(f"| {category} | {category_counts[category]} |")

    lines.extend(
        [
            "",
            "## Priority Counts",
            "",
            "| priority | count |",
            "| --- | --- |",
            f"| high | {priority_counts['high']} |",
            f"| medium | {priority_counts['medium']} |",
            f"| low | {priority_counts['low']} |",
            "",
            "## High Priority Dependencies",
            "",
            "| groupId | artifactId | version | scope | categories | reason |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    if high_priority_rows:
        for record in high_priority_rows:
            lines.append(classified_dependency_markdown_row(record))
    else:
        lines.append("| 없음 | 없음 | 없음 | 없음 | 없음 | 없음 |")

    lines.extend(
        [
            "",
            "## Unknown Dependencies",
            "",
            "| groupId | artifactId | version | scope | categories | reason |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )

    if unknown_rows:
        for record in unknown_rows:
            lines.append(classified_dependency_markdown_row(record))
    else:
        lines.append("| 없음 | 없음 | 없음 | 없음 | 없음 | 없음 |")

    lines.extend(
        [
            "",
            "## Next Step",
            "",
            "High priority dependency를 우선 대상으로 Qwen에게 eGovFrame 4.3 대응 추천을 요청한다.",
            "",
        ]
    )
    path.write_text("\n".join(lines), encoding="utf-8")


def classified_dependency_markdown_row(record: ClassifiedDependencyRecord) -> str:
    return (
        f"| {escape_markdown_cell(record.group_id)} | "
        f"{escape_markdown_cell(record.artifact_id)} | "
        f"{escape_markdown_cell(record.version)} | "
        f"{escape_markdown_cell(record.scope)} | "
        f"{escape_markdown_cell(';'.join(record.categories))} | "
        f"{escape_markdown_cell(record.reason)} |"
    )


def escape_markdown_cell(value: str) -> str:
    return value.replace("|", "\\|") if value else ""


def count_categories(rows: Sequence[ClassifiedDependencyRecord]) -> dict[str, int]:
    counts = {category: 0 for category in CATEGORY_ORDER}
    for record in rows:
        for category in record.categories:
            counts[category] += 1
    return counts


def count_priorities(rows: Sequence[ClassifiedDependencyRecord]) -> dict[str, int]:
    counts = {"high": 0, "medium": 0, "low": 0}
    for record in rows:
        counts[record.priority] += 1
    return counts


def count_unknown_dependencies(rows: Sequence[ClassifiedDependencyRecord]) -> int:
    return sum(1 for record in rows if "unknown" in record.categories)


def write_summary(path: Path, result: AnalysisResult) -> None:
    dependency_counter = Counter(
        record.artifact_id for record in result.dependencies if record.artifact_id
    )
    egov_dependencies = [
        record
        for record in result.dependencies
        if record.group_id in {"egovframework", "org.egovframe"}
        or record.group_id.startswith("egovframework.")
        or record.group_id.startswith("org.egovframe.")
    ]
    mybatis_dependencies = [
        record
        for record in result.dependencies
        if "ibatis" in record.artifact_id.lower() or "mybatis" in record.artifact_id.lower()
    ]
    priority_counts = count_priorities(result.classified_dependencies)
    unknown_count = count_unknown_dependencies(result.classified_dependencies)

    lines: list[str] = [
        "## Summary",
        "",
        f"- pom.xml 개수: {result.pom_count}",
        f"- dependency 개수: {len(result.dependencies)}",
        f"- dependencyManagement 개수: {len(result.dependency_management)}",
        f"- exclusion 개수: {len(result.exclusions)}",
        f"- property 개수: {len(result.properties)}",
        f"- parent pom 개수: {len(result.parents)}",
        "",
        "## Category Summary",
        "",
        f"- high priority dependency 수: {priority_counts['high']}",
        f"- medium priority dependency 수: {priority_counts['medium']}",
        f"- low priority dependency 수: {priority_counts['low']}",
        f"- unknown dependency 수: {unknown_count}",
        "- 상세 분류 결과: output/pom-analysis/dependency-category-summary.md",
        "",
        "## Dependency Top 20",
        "",
    ]

    if dependency_counter:
        for artifact_id, count in dependency_counter.most_common(20):
            lines.append(f"- {artifact_id}: {count}")
    else:
        lines.append("- 없음")

    lines.extend(
        [
            "",
            "## eGovFrame Dependency",
            "",
        ]
    )
    if egov_dependencies:
        for record in egov_dependencies:
            lines.append(
                f"- {record.group_id}:{record.artifact_id}:{record.version or '(no version)'}"
            )
    else:
        lines.append("- 없음")

    lines.extend(
        [
            "",
            "## MyBatis 관련",
            "",
        ]
    )
    if mybatis_dependencies:
        for record in mybatis_dependencies:
            lines.append(
                f"- {record.group_id}:{record.artifact_id}:{record.version or '(no version)'}"
            )
    else:
        lines.append("- 없음")

    if result.errors:
        lines.extend(["", "## Errors", ""])
        for error in result.errors:
            lines.append(f"- {error}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, IsADirectoryError, ValueError) as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)
