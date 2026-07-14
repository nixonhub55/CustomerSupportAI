from assistants.base_assistant import BaseAssistant


class BillingAssistant(BaseAssistant):

    name = "billing"

    plugin = "billing"

    system_prompt = """
You are a billing customer support AI.

Be polite.

Answer using the provided context.

Never invent customer information.
"""

    tools = [
        "customer_lookup",
        "payment_history",
        "invoice_summary",
        "ticket_summary"
    ]