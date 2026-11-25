# === Stage 7: Генерация идентификаторов ===
# Project: ComicShelf
import uuid
from collections.abc import Hashable


PROJECT_PREFIX = "cs"


class IdentifierCollisionError(Exception):
    """Raised when a generated identifier already exists in a registry."""


class IdentifierRegistry:
    """Maintains a set of unique identifiers with collision checking."""

    def __init__(self):
        self._ids = set()

    def generate(self, kind: Hashable) -> str:
        """Create a unique prefixed identifier and register it."""
        while True:
            candidate = f"{PROJECT_PREFIX}:{kind}:{uuid.uuid4().hex}"
            if candidate not in self._ids:
                self._ids.add(candidate)
                return candidate

    def register(self, identifier: Hashable) -> None:
        if identifier in self._ids:
            raise IdentifierCollisionError(identifier)
        self._ids.add(identifier)

    def is_available(self, identifier: Hashable) -> bool:
        return identifier not in self._ids

    def __len__(self) -> int:
        return len(self._ids)
