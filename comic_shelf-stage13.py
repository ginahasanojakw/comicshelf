# === Stage 13: Быстрые фильтры ===
# Project: ComicShelf
from datetime import date


def _parse_issue_field(value):
    if value is None:
        return None
    if isinstance(value, (date,)):
        return value
    if isinstance(value, str):
        cleaned = value.strip()
        if cleaned.endswith("-01"):
            return date.fromisoformat(cleaned[:7])
        try:
            return date.fromisoformat(cleaned)
        except ValueError:
            return None
    return None


def issues_today(issues, today=None):
    today = today or date.today()
    result = []
    for issue in issues:
        released = _parse_issue_field(getattr(issue, "released", None))
        if released and released == today:
            result.append(issue)
    return result


def issues_this_week(issues, today=None):
    today = today or date.today()
    start = today - __import__("datetime").timedelta(days=today.weekday())
    result = []
    for issue in issues:
        released = _parse_issue_field(getattr(issue, "released", None))
        if released and start <= released <= today:
            result.append(issue)
    return result


def issues_overdue(issues):
    result = []
    for issue in issues:
        released = _parse_issue_field(getattr(issue, "released", None))
        if released is None:
            continue
        status = getattr(issue, "status", None)
        if status and status.lower() == "released" and released < date.today():
            result.append(issue)
    return result
