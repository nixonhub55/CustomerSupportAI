from assistants.base_assistant import BaseAssistant


class BillingAssistant(BaseAssistant):

    NAME = "billing"

    DISPLAY_NAME = "Billing Assistant"

    DESCRIPTION = "Customer billing support assistant."

    CATEGORY = "assistant"

    PLUGIN = "billing"

    SYSTEM_PROMPT = """
You are a billing customer support AI.

Be polite.

Answer using the provided context.

Never invent customer information.
"""

    TOOLS = [
        "customer_lookup",
        "payment_history",
        "invoice_summary",
        "ticket_summary",
        "customer_statistics"
    ]