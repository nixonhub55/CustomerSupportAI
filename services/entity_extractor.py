import re

from core.logger import Logger


def extract_entities(question: str):

    Logger.debug(
        f"Extracting entities: {question}"
    )

    entities = {}

    # ----------------------------
    # Account Number
    # ----------------------------

    match = re.search(
        r"\b\d{6,12}\b",
        question
    )

    if match:

        entities["account_no"] = match.group()

    # ----------------------------
    # Customer
    # ----------------------------

    if any(word in question for word in [

        "customer",
        "account"

    ]):

        entities["customer"] = True

    # ----------------------------
    # Invoice
    # ----------------------------

    if any(word in question for word in [

        "invoice",
        "bill",
        "balance"

    ]):

        entities["invoice"] = True

    # ----------------------------
    # Payment
    # ----------------------------

    if any(word in question for word in [

        "payment",
        "paid",
        "history"

    ]):

        entities["payment"] = True

    # ----------------------------
    # Ticket
    # ----------------------------

    if any(word in question for word in [

        "ticket",
        "case",
        "complaint"

    ]):

        entities["ticket"] = True

    # ----------------------------
    # Customer List
    # ----------------------------

    if any(text in question for text in [

        "all customers",
        "list customers",
        "customer list",
        "show customers",
        "all customer",
        "all account"

    ]):

        entities["customer_list"] = True

    # ----------------------------
    # Statistics
    # ----------------------------

    if any(text in question for text in [

        "how many",
        "count",
        "total customers",
        "number of customers"

    ]):

        entities["statistics"] = True

    Logger.debug(
        f"Entities: {entities}"
    )

    return entities