import re


def normalize(question: str) -> str:

    question = question.lower().strip()

    question = re.sub(r"[^\w\s]", " ", question)

    question = re.sub(r"\s+", " ", question)

    replacements = {
        "acct": "account",
        "acc": "account",
        "acct.": "account",
        "cust": "customer",
        "cust.": "customer",
        "email address": "email",
        "account no": "account number",
        "account_no": "account number"
    }

    for old, new in replacements.items():
        question = question.replace(old, new)

    return question.strip()