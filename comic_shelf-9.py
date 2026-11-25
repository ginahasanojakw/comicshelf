# === Stage 9: Текстовый поиск ===
# Project: ComicShelf
import re


def highlight(text: str, pattern: str) -> str:
    """Return text with all occurrences of pattern wrapped in ANSI tags.

    The search is case-insensitive, so the pattern is lower-cased before
    matching while the original characters are preserved in the output.
    """
    if not text or not pattern:
        return text

    lowered = text.lower()
    needle = pattern.lower()
    if needle not in lowered:
        return text

    marker = "\033[31m\033[1m"
    reset = "\033[0m"
    prefix = "\033[39m"

    def repl(match):
        return marker + match.group(0) + reset

    return prefix + re.sub(re.escape(needle), repl, lowered)
