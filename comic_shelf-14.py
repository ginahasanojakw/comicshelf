# === Stage 14: Избранное ===
# Project: ComicShelf
from typing import Dict, List, Set


class Issue:
    """A single comic issue with a favorite flag."""

    def __init__(self, title: str, issue_number: int, publisher: str) -> None:
        self.title = title
        self.issue_number = issue_number
        self.publisher = publisher
        self.is_favorite = False

    def set_favorite(self, value: bool) -> None:
        """Toggle or set the favorite flag."""
        self.is_favorite = bool(value)

    def is_favorited(self) -> bool:
        """Return the current favorite flag."""
        return self.is_favorite

    def __repr__(self) -> str:
        return (
            f"Issue(title={self.title!r}, "
            f"issue_number={self.issue_number}, "
            f"publisher={self.publisher!r}, "
            f"is_favorite={self.is_favorite})"
        )


class FavoriteManager:
    """Track favorite issues for a collection."""

    def __init__(self, issues: List[Issue] | None = None) -> None:
        self._issues: List[Issue] = issues if issues is not None else []

    def add_issue(self, issue: Issue) -> None:
        """Append an issue to the tracked collection."""
        self._issues.append(issue)

    def toggle_favorite(self, issue: Issue) -> None:
        """Mark an issue as favorite or remove the favorite mark."""
        if issue in self._issues:
            issue.set_favorite(not issue.is_favorited)

    def set_favorite(self, issue: Issue) -> None:
        """Explicitly mark an issue as favorite."""
        if issue in self._issues:
            issue.set_favorite(True)

    def remove_favorite(self, issue: Issue) -> None:
        """Explicitly remove the favorite mark from an issue."""
        if issue in self._issues:
            issue.set_favorite(False)

    def favorite_issues(self) -> List[Issue]:
        """Return the list of currently favorited issues."""
        return [issue for issue in self._issues if issue.is_favorited()]

    def favorite_ids(self) -> Set[int]:
        """Return a set of identifiers for favorited issues."""
        return {issue.issue_number for issue in self.favorite_issues()}

    def count_favorites(self) -> int:
        """Return the number of favorited issues."""
        return len(self.favorite_issues())

    def is_favorited(self, issue: Issue) -> bool:
        """Check whether an issue is currently favorited."""
        return issue in self.favorite_issues()

    def __len__(self) -> int:
        return len(self._issues)
