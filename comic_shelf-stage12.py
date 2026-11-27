# === Stage 12: Группировка ===
# Project: ComicShelf
from collections import Counter


def group_issues_by_number(issues):
    """Group issues by their 'number' field and count occurrences in each group."""
    return Counter(issue["number"] for issue in issues)


def grouped_issue_counts(issues):
    """Group issues by 'number' and return a list of (number, count) tuples sorted by number."""
    grouped = group_issues_by_number(issues)
    return sorted(grouped.items(), key=lambda item: item[0])


def count_skipped_ranges(issues):
    """Count distinct issue numbers present, used as input for gap analysis."""
    return len(group_issues_by_number(issues))


def find_missing_numbers(issue_numbers):
    """Find gaps in a sorted sequence of issue numbers."""
    sorted_numbers = sorted(issue_numbers)
    if not sorted_numbers:
        return []

    missing = []
    for start, end in zip(sorted_numbers[:-1], sorted_numbers[1:]):
        if end - start > 1:
            missing.extend(range(start + 1, end))
    return missing


def summarize_series(series):
    """Summarize a series by grouping its issues by number and reporting counts."""
    issues = series.get("issues", [])
    grouped = grouped_issue_counts(issues)
    total = len(issues)
    return {
        "title": series["title"],
        "publisher": series["publisher"],
        "total_issues": total,
        "distinct_numbers": len(grouped),
        "number_counts": grouped,
    }


def build_index_by_number(issues):
    """Build a lookup mapping each issue number to the list of issues sharing it."""
    grouped = group_issues_by_number(issues)
    index = {}
    for number, count in grouped.items():
        index[number] = [issue for issue in issues if issue["number"] == number]
    return index
