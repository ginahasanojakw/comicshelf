# === Stage 3: Хранилище в памяти ===
# Project: ComicShelf
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Issue:
    title: str
    number: int
    publisher: str
    status: str

    def __post_init__(self) -> None:
        if not isinstance(self.number, int):
            raise TypeError("Issue number must be an integer")
        if self.status not in ("published", "ongoing", "upcoming", "cancelled"):
            raise ValueError(
                f"Unknown status {self.status!r}; "
                "expected one of published, ongoing, upcoming, cancelled"
            )


class IssueStore:
    def __init__(self) -> None:
        self._by_id: Dict[str, Issue] = {}
        self._counter = 0

    def add(self, issue: Issue) -> str:
        identifier = str(self._counter)
        self._counter += 1
        self._by_id[identifier] = issue
        return identifier

    def get(self, identifier: str) -> Optional[Issue]:
        return self._by_id.get(identifier)

    def all(self) -> List[Issue]:
        return list(self._by_id.values())

    def count(self) -> int:
        return len(self._by_id)

    def remove(self, identifier: str) -> bool:
        return self._by_id.pop(identifier, None) is not None

    def identifiers(self) -> List[str]:
        return list(self._by_id.keys())
