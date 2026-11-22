# === Stage 1: Каркас модуля ===
# Project: ComicShelf
from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class Issue:
    title: str
    number: str
    publisher: str
    status: str


def make_sample_issues() -> List[Issue]:
    return [
        Issue("Action Comics", "1", "DC Comics", "complete"),
        Issue("Amazing Spider-Man", "1", "Marvel", "complete"),
        Issue("Sandman", "1", "DC Comics", "cancelled"),
        Issue("Watchmen", "1", "DC Comics", "complete"),
        Issue("Saga", "1", "Image Comics", "ongoing"),
    ]


def main() -> None:
    issues = make_sample_issues()
    print("ComicShelf Collection")
    print(f"Total issues: {len(issues)}")
    for issue in issues:
        print(f"{issue.title} #{issue.number} ({issue.publisher}) - {issue.status}")


if __name__ == "__main__":
    main()
