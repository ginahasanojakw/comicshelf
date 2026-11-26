# === Stage 11: Теги ===
# Project: ComicShelf
from typing import Dict, List, Optional


class Tag:
    def __init__(self, name: str) -> None:
        if not name:
            raise ValueError("tag name cannot be empty")
        self.name = name

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Tag) and other.name == self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return f"Tag({self.name!r})"


class Issue:
    def __init__(
        self,
        title: str,
        number: int,
        publisher: str,
        status: str,
        tags: Optional[List[Tag]] = None,
    ) -> None:
        self.title = title
        self.number = number
        self.publisher = publisher
        self.status = status
        self.tags: set[Tag] = set(tags) if tags else set()

    def add_tag(self, tag: Tag) -> None:
        self.tags.add(tag)

    def remove_tag(self, tag: Tag) -> None:
        self.tags.discard(tag)

    def has_tag(self, tag: Tag) -> bool:
        return tag in self.tags

    def tag_names(self) -> List[str]:
        return sorted(tag.name for tag in self.tags)

    def find_tag(self, name: str) -> Optional[Tag]:
        for tag in self.tags:
            if tag.name == name:
                return tag
        return None

    def __repr__(self) -> str:
        return (
            f"Issue(title={self.title!r}, number={self.number}, "
            f"publisher={self.publisher!r}, status={self.status!r}, "
            f"tags={self.tag_names()})"
        )


def search_by_tag(
    issues: List[Issue], tag_name: str
) -> List[Issue]:
    return [issue for issue in issues if issue.has_tag(Tag(tag_name))]


def search_by_tag_names(
    issues: List[Issue], names: List[str]
) -> List[Issue]:
    wanted = {name.strip().lower() for name in names if name.strip()}
    if not wanted:
        return list(issues)

    def matches(issue: Issue) -> bool:
        return any(
            issue.tag.name.strip().lower() in wanted for issue.tag in issue.tags
        )

    return [issue for issue in issues if matches(issue)]
