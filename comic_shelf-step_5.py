# === Stage 5: Связанная сущность ===
# Project: ComicShelf
import hashlib


class Series:
    """A comic book series consisting of one or more issues."""

    def __init__(self, name, publisher):
        self._id = self._generate_id(name, publisher)
        self.name = name
        self.publisher = publisher
        self._issues = []

    @staticmethod
    def _generate_id(name, publisher):
        digest = hashlib.sha256()
        digest.update(name.encode("utf-8"))
        digest.update(b"\x00")
        digest.update(publisher.encode("utf-8"))
        return digest.hexdigest()[:16]

    def add_issue(self, issue_id):
        self._issues.append(issue_id)
        return self

    def remove_issue(self, issue_id):
        if issue_id in self._issues:
            self._issues.remove(issue_id)
            return True
        return False

    def issue_ids(self):
        return list(self._issues)

    def __repr__(self):
        return f"Series(id={self._id!r}, name={self.name!r}, publisher={self.publisher!r}, issues={self.issue_ids()})"
