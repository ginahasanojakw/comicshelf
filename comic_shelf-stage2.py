# === Stage 2: Проверка полей ===
# Project: ComicShelf
from typing import Optional


ALLOWED_PUBLISHERS = {"DC", "Marvel", "Image", "Indies", "Unknown"}
VALID_STATES = ("complete", "ongoing", "hiatus", "cancelled", "unreleased")


def normalize_publisher(raw: str) -> str:
    if not raw:
        return "Unknown"
    return raw.strip().upper()


def normalize_state(raw: str) -> str:
    if not raw:
        return "Unknown"
    return raw.strip().lower()


def normalize_issue_number(raw: str) -> int:
    text = raw.strip()
    if not text:
        raise ValueError("issue number is empty")
    digits = "".join(ch for ch in text if ch.isdigit())
    if not digits:
        raise ValueError("issue number contains no digits")
    return int(digits)


def validate_issue(title: str, issue_number: str, publisher: str, state: str) -> None:
    if not title or not title.strip():
        raise ValueError("issue title must not be empty")
    if not issue_number or not issue_number.strip():
        raise ValueError("issue number must not be empty")
    if not publisher or not publisher.strip():
        raise ValueError("publisher must not be empty")
    if not state or not state.strip():
        raise ValueError("issue state must not be empty")
    normalized_publisher = normalize_publisher(publisher)
    if normalized_publisher not in ALLOWED_PUBLISHERS:
        raise ValueError(
            f"publisher '{normalized_publisher}' is not supported"
        )
    normalized_state = normalize_state(state)
    if normalized_state not in VALID_STATES:
        raise ValueError(
            f"state '{normalized_state}' is not valid, "
            f"expected one of {', '.join(VALID_STATES)}"
        )
    normalized_issue_number = normalize_issue_number(issue_number)
    if normalized_issue_number <= 0:
        raise ValueError("issue number must be a positive integer")
