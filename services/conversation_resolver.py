from core.logger import Logger


class ConversationResolver:

    CUSTOMER_REFERENCES = [
        "he",
        "him",
        "his",
        "she",
        "her",
        "hers",
        "they",
        "them",
        "their",
        "customer",
        "account",
        "this customer",
        "that customer",
        "this account",
        "that account",
        "the customer",
        "the account",
        "same customer",
        "same account"
    ]

    def __init__(self, context):
        self.context = context

    def resolve(self, question):

        Logger.debug("=" * 50)
        Logger.debug("ConversationResolver")

        memory = self.context.all()

        Logger.debug(f"Memory: {memory}")

        if not memory:
            Logger.debug("No memory found.")
            return question

        account_no = memory.get("account_no")

        Logger.debug(f"Account: {account_no}")

        if not account_no:
            Logger.debug("No account in memory.")
            return question

        lower = question.lower()

        Logger.debug(f"Question: {lower}")

        matched = any(
            ref in lower
            for ref in self.CUSTOMER_REFERENCES
        )

        Logger.debug(f"Matched reference: {matched}")

        if matched:

            resolved = (
                f"{question} (customer {account_no})"
            )

            Logger.debug(f"Resolved: {resolved}")

            return resolved

        Logger.debug("No customer reference detected.")

        return question