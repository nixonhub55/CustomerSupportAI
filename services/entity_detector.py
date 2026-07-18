PRONOUNS = [
    "his",
    "her",
    "their",
    "them",
    "that customer",
    "this customer",
    "that account",
    "this account"
]


def has_customer_reference(question):

    q = question.lower()

    if "customer" in q:
        return True

    if "account" in q:
        return True

    return any(p in q for p in PRONOUNS)