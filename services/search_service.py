import re


STOP_WORDS = {
    "the",
    "is",
    "a",
    "an",
    "to",
    "for",
    "of",
    "using",
    "how",
    "what",
    "can",
    "i",
    "my"
}


def extract_keywords(question):

    words = re.findall(r"\w+", question.lower())

    keywords = []

    for word in words:

        if word not in STOP_WORDS:

            keywords.append(word)

    return keywords