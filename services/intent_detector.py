import re

from core.logger import Logger


INTENTS = {

    "greeting": [
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening"
    ],

    "gratitude": [
        "thanks",
        "thank you",
        "thank u"
    ],

    "farewell": [
        "bye",
        "goodbye",
        "see you"
    ],

    "customer_support": []

}


def contains_phrase(text: str, phrase: str) -> bool:
    """
    Matches complete words or phrases only.

    Examples:
        hi      -> matches "hi"
        hi      -> NOT "his"
        bye     -> NOT "byebye"
        thank you -> matches "thank you"
    """

    pattern = r"\b" + re.escape(phrase) + r"\b"

    return re.search(
        pattern,
        text,
        flags=re.IGNORECASE
    ) is not None


def detect_intent(question: str) -> str:

    question = question.lower().strip()

    Logger.debug(
        f"Detecting intent: {question}"
    )

    for intent, keywords in INTENTS.items():

        for keyword in keywords:

            if contains_phrase(question, keyword):

                Logger.debug(
                    f"Detected intent: {intent}"
                )

                return intent

    Logger.debug(
        "Detected intent: customer_support"
    )

    return "customer_support"