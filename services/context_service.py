from memory.session import session

from services.database_service import (
    get_customer_profile,
    format_customer
)

from services.knowledge_service import get_knowledge


def build_context(action, question):

    customer = None
    customer_text = ""

    if action["account_no"]:
        customer = get_customer_profile(action["account_no"])

        if customer:
            customer_text = format_customer(customer)

    knowledge = ""

    if action["knowledge"]:
        knowledge = get_knowledge(question)

    return {
        "customer": customer,
        "customer_text": customer_text,
        "knowledge": knowledge
    }