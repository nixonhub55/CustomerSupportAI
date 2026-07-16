from ai.provider_manager import ProviderManager


class AI:

    def __init__(self):

        self.manager = ProviderManager()

    # -----------------------------------------------------

    def ask(
        self,
        assistant,
        question,
        execution_plan,
        context
    ):

        prompt = f"""
{assistant.SYSTEM_PROMPT}

Intent:
{execution_plan.intent}

Context:
{context}

Customer Question:
{question}

Instructions:

- Answer using the context whenever possible.
- If the context is empty, answer from general customer support knowledge.
- Never invent customer-specific information.
- Be concise and professional.
"""

        return self.manager.ask(prompt)