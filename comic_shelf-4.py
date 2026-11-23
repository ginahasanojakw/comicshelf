# === Stage 4: Удаление и восстановление ===
# Project: ComicShelf
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, Optional


class ComicStatus(str, Enum):
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    DROPPED = "dropped"


@dataclass
class Issue:
    title: str
    number: int
    publisher: str
    status: ComicStatus = ComicStatus.ACTIVE
    deleted: bool = False

    def __post_init__(self):
        if self.status not in ComicStatus:
            raise ValueError(f"Invalid status: {self.status}")


@dataclass
class Series:
    name: str
    issues: Dict[int, Issue] = field(default_factory=dict)


class ComicShelf:
    def __init__(self):
        self.series: Dict[str, Series] = {}

    def add_issue(self, series_name: str, issue: Issue) -> None:
        self.series.setdefault(series_name, Series(name=series_name))
        self.series[series_name].issues[issue.number] = issue

    def remove_issue(self, series_name: str, number: int) -> Optional[Issue]:
        series = self.series.get(series_name)
        if not series:
            return None
        issue = series.issues.pop(number, None)
        if issue is not None:
            issue.deleted = True
        return issue

    def restore_issue(self, series_name: str, number: int) -> bool:
        series = self.series.get(series_name)
        if not series:
            return False
        issue = series.issues.get(number)
        if issue is None:
            return False
        issue.deleted = False
        return True

    def active_issues(self, series_name: str) -> list:
        series = self.series.get(series_name)
        if not series:
            return []
        return [
            issue for issue in series.issues.values()
            if not issue.deleted and issue.status == ComicStatus.ACTIVE
        ]

    def soft_delete_all(self, series_name: str) -> None:
        series = self.series.get(series_name)
        if series:
            for issue in series.issues.values():
                issue.deleted = True
