import re


def plan(question):

    q = question.lower()

    plan = {
        "customer": False,
        "knowledge": False,
        "account_no": None,
        "phone": None,
        "intent": "UNKNOWN"
    }

    # Detect account number (6-9 digits for your system)
    account = re.search(r"\b\d{6,9}\b", q)

    if account:
        plan["account_no"] = account.group()

    # Detect Philippine mobile number
    phone = re.search(r"\b09\d{8}\b", q)

    if phone:
        plan["phone"] = phone.group()

    # Customer lookup
    if any(word in q for word in [
        "show customer",
        "customer info",
        "customer information",
        "customer details",
        "account details",
        "show account",
        "who is",
        "who owns",
        "phone number"
    ]):
        plan["customer"] = True
        plan["intent"] = "CUSTOMER_LOOKUP"

    elif "balance" in q:
        plan["customer"] = True
        plan["intent"] = "BALANCE"

    elif "plan" in q:
        plan["customer"] = True
        plan["intent"] = "PLAN"

    elif any(word in q for word in ["status", "active", "inactive"]):
        plan["customer"] = True
        plan["intent"] = "STATUS"

    elif any(word in q for word in ["payment", "gcash", "maya", "pay"]):
        plan["knowledge"] = True
        plan["intent"] = "PAYMENT"

    elif any(word in q for word in ["policy", "process", "how", "why", "when"]):
        plan["knowledge"] = True
        plan["intent"] = "KNOWLEDGE"

    return plan