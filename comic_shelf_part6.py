# === Stage 6: Связи между сущностями ===
# Project: ComicShelf
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Issue:
    title: str
    number: int
    publisher: str
    status: str


@dataclass(frozen=True)
class Series:
    name: str
    issues: List[Issue] = field(default_factory=list)


def build_series_index(series: Series) -> dict:
    return {issue.title: issue for issue in series.issues}


def find_all_issues_for_issue(series: Series, target_title: str, target_number: int) -> Optional[Issue]:
    index = build_series_index(series)
    return index.get(target_title)


def verify_issue_belongs_to_series(
    series: Series,
    target_title: str,
    target_number: int,
) -> bool:
    index = build_series_index(series)
    if target_title not in index:
        return False
    return index[target_title].number == target_number


def verify_series_integrity(series: Series) -> bool:
    seen_titles = set()
    for issue in series.issues:
        if issue.title in seen_titles:
            return False
        seen_titles.add(issue.title)
        if not issue.title or not isinstance(issue.number, int):
            return False
        if not issue.publisher or not issue.status:
            return False
    return True


def find_all_issues_for_issue_wrapper(series: Series, target_title: str) -> List[Issue]:
    index = build_series_index(series)
    return list(index.get(target_title, [])) if isinstance(index.get(target_title), list) else []


if __name__ == "__main__":
    sample = Series(
        name="Detective Comics",
        issues=[
            Issue(title="Detective Comics #1", number=1, publisher="DC", status="published"),
            Issue(title="Detective Comics #2", number=2, publisher="DC", status="published"),
        ],
    )

    print(verify_series_integrity(sample))
    print(verify_issue_belongs_to_series(sample, "Detective Comics #1", 1))
    print(find_all_issues_for_issue(sample, "Detective Comics #1").number)
