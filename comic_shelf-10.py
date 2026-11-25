# === Stage 10: Поиск по нескольким словам ===
# Project: ComicShelf
from collections import Counter


def parse_query(text):
    """Parse a search query into a set of include terms and exclude terms.

    A leading '-' marks an exclusion term. Surrounding whitespace is stripped.
    Empty tokens are ignored.
    """
    includes = set()
    excludes = set()
    for token in text.replace('-', ' - ').split():
        token = token.strip('-')
        if not token:
            continue
        if token.startswith('-'):
            excludes.add(token[1:].strip())
        else:
            includes.add(token)
    return includes, excludes


def matches_issue(issue, includes, excludes):
    haystack = set((issue.title or '').lower().split())
    haystack |= {str(issue.number).lower()}
    haystack |= {issue.publisher.lower()}
    haystack |= {issue.status.lower()}
    if excludes & haystack:
        return False
    return not includes or includes <= haystack


def search_issues(issues, query):
    includes, excludes = parse_query(query)
    return [issue for issue in issues if matches_issue(issue, includes, excludes)]


class Issue:
    def __init__(self, title, number, publisher, status):
        self.title = title
        self.number = number
        self.publisher = publisher
        self.status = status


if __name__ == "__main__":
    data = [
        Issue("Amazing World", 1, "ACME", "in-print"),
        Issue("Amazing World", 5, "ACME", "discontinued"),
        Issue("Silent City", 12, "Nova", "in-print"),
        Issue("Silent City", 1, "Nova", "in-print"),
    ]
    print([i.title for i in search_issues(data, "amazing acme")])
    print([i.title for i in search_issues(data, "amazing -acme")])
    print([i.title for i in search_issues(data, "-amazing")])
    print([i.title for i in search_issues(data, "amazing -acme -world")])
