import re


def plan(question):

    q = question.lower()

    plan = {
        "customer": False,
        "knowledge": False,
        "account_no": None,
        "intent": "UNKNOWN"
    }

    # Find account number
    match = re.search(r"\b\d{6,12}\b", q)

    if match:
        plan["account_no"] = match.group()

    # Customer lookup
    if any(word in q for word in [
        "show customer",
        "customer info",
        "customer information",
        "customer details",
        "account details",
        "show account"
    ]):
        plan["customer"] = True
        plan["intent"] = "CUSTOMER_LOOKUP"

    # Balance
    elif "balance" in q:
        plan["customer"] = True
        plan["intent"] = "BALANCE"

    # Plan
    elif "plan" in q:
        plan["customer"] = True
        plan["intent"] = "PLAN"

    # Status
    elif any(word in q for word in ["status", "active", "inactive"]):
        plan["customer"] = True
        plan["intent"] = "STATUS"

    # Payment questions
    elif any(word in q for word in ["payment", "gcash", "maya", "pay"]):
        plan["knowledge"] = True
        plan["intent"] = "PAYMENT"

    # Policy / process questions
    elif any(word in q for word in ["policy", "process", "how", "why", "when"]):
        plan["knowledge"] = True
        plan["intent"] = "KNOWLEDGE"

    return plan