from assistants.base_assistant import BaseAssistant


class BillingAssistant(BaseAssistant):

    NAME = "billing"

    DISPLAY_NAME = "Billing Assistant"

    DESCRIPTION = "Customer billing support."

    PLUGIN = "billing"

    SYSTEM_PROMPT = """
You are an experienced billing customer support representative.

Be polite.

Be professional.

Answer ONLY using the retrieved context.

Never invent customer information.

If the information is unavailable,
say so politely.
"""

    TOOLS = [

        "customer_lookup",

        "payment_history",

        "invoice_summary",

        "ticket_summary"
    ]