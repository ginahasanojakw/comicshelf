# === Stage 8: Фильтрация записей ===
# Project: ComicShelf
from datetime import date


def parse_number(value):
    parts = str(value).split()
    if len(parts) < 2:
        return None, None
    try:
        return int(parts[0]), int(parts[1])
    except ValueError:
        return None, None


def number_matches(issue, target_number):
    if target_number is None:
        return True
    issue_number, total = parse_number(issue.get("number"))
    if issue_number is None:
        return False
    return issue_number == target_number


def filter_by_number(issues, target_number):
    return [issue for issue in issues if number_matches(issue, target_number)]


def parse_date(value):
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%B %d, %Y", "%b %d, %Y"):
        try:
            return date.fromisoformat(text.replace(".", "-"))
        except ValueError:
            pass
    try:
        return date(*map(int, text.split("-")))
    except (ValueError, TypeError):
        return None


def date_matches(issue, low, high):
    issue_date = parse_date(issue.get("date"))
    if issue_date is None:
        return False
    if low is not None and issue_date < low:
        return False
    if high is not None and issue_date > high:
        return False
    return True


def filter_by_date_range(issues, low=None, high=None):
    return [issue for issue in issues if date_matches(issue, low, high)]


def filter_issues(issues, target_number=None, low=None, high=None):
    result = filter_by_number(issues, target_number)
    return filter_by_date_range(result, low, high)


def find_gaps(start_number, end_number, issues):
    present = set()
    for issue in issues:
        issue_number, _ = parse_number(issue.get("number"))
        if issue_number is not None:
            present.add(issue_number)
    return [n for n in range(start_number, end_number + 1) if n not in present]
