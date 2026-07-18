import re


def has_word(text: str, word: str) -> bool:
    """
    Returns True only if the whole word exists.
    Example:
        has_word("hi there", "hi") -> True
        has_word("history", "hi") -> False
        has_word("his balance", "hi") -> False
    """

    return re.search(
        rf"\b{re.escape(word.lower())}\b",
        text.lower()
    ) is not None


def contains_any(text: str, words: list[str]) -> bool:
    """
    Returns True if any whole word exists.
    """

    return any(
        has_word(text, word)
        for word in words
    )


def extract_account_no(text: str):

    match = re.search(
        r"\b\d{6,12}\b",
        text
    )

    if match:
        return match.group()

    return None